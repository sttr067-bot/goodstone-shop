/**
 * GOODSTONE Cloud Sync Engine (Firebase Realtime Database)
 * Enables real-time synchronization between Admin (PC/Mobile) and Customer Storefront.
 */

// Shared default Firebase config placeholder (can be overridden in admin or localStorage)
let cloudDb = null;
let isCloudConnected = false;

function getFirebaseConfig() {
    const saved = localStorage.getItem("goodstone_firebase_config");
    if (saved) {
        try {
            return JSON.parse(saved);
        } catch (e) {
            console.error("Invalid saved firebase config", e);
        }
    }
    // Check if global GOODSTONE_FIREBASE_CONFIG is defined
    if (typeof GOODSTONE_FIREBASE_CONFIG !== "undefined" && GOODSTONE_FIREBASE_CONFIG.apiKey) {
        return GOODSTONE_FIREBASE_CONFIG;
    }
    return null;
}

function initCloudDatabase(onReadyCallback) {
    const config = getFirebaseConfig();
    if (!config || !config.apiKey || !config.databaseURL) {
        console.log("ℹ️ Cloud Database: Not configured yet. Running in local storage mode.");
        isCloudConnected = false;
        if (typeof onCloudStatusChange === "function") onCloudStatusChange(false);
        if (typeof onReadyCallback === "function") onReadyCallback(null);
        return;
    }

    try {
        if (!firebase.apps.length) {
            firebase.initializeApp(config);
        }
        cloudDb = firebase.database();
        isCloudConnected = true;
        console.log("✅ Cloud Database: Connected to Firebase Realtime Database!");
        if (typeof onCloudStatusChange === "function") onCloudStatusChange(true);
        if (typeof onReadyCallback === "function") onReadyCallback(cloudDb);
    } catch (err) {
        console.error("❌ Cloud Database Init Error:", err);
        isCloudConnected = false;
        if (typeof onCloudStatusChange === "function") onCloudStatusChange(false, err.message);
        if (typeof onReadyCallback === "function") onReadyCallback(null);
    }
}

// Push products from local to Cloud
async function syncProductsToCloud(productsArray) {
    if (!cloudDb) return false;
    try {
        await cloudDb.ref("products").set(productsArray);
        console.log("☁️ Products successfully synced to Cloud Database!");
        return true;
    } catch (e) {
        console.error("Failed to sync products to cloud:", e);
        return false;
    }
}

// Push a new order to Cloud
async function submitOrderToCloud(orderObj) {
    if (!cloudDb) return false;
    try {
        await cloudDb.ref("orders/" + orderObj.id).set(orderObj);
        console.log("☁️ Order successfully submitted to Cloud Database:", orderObj.id);
        return true;
    } catch (e) {
        console.error("Failed to submit order to cloud:", e);
        return false;
    }
}

// Listen for live product updates
function listenToCloudProducts(callback) {
    if (!cloudDb) return;
    cloudDb.ref("products").on("value", snapshot => {
        const data = snapshot.val();
        if (data && Array.isArray(data) && data.length > 0) {
            console.log("☁️ Live products updated from Cloud Database:", data.length, "items");
            localStorage.setItem("goodstone_products", JSON.stringify(data));
            if (typeof callback === "function") callback(data);
        }
    });
}

// Listen for live orders (for admin & tracking)
function listenToCloudOrders(callback) {
    if (!cloudDb) return;
    cloudDb.ref("orders").on("value", snapshot => {
        const val = snapshot.val();
        const ordersArray = [];
        if (val) {
            Object.keys(val).forEach(k => {
                ordersArray.push(val[k]);
            });
        }
        console.log("☁️ Live orders updated from Cloud Database:", ordersArray.length, "orders");
        localStorage.setItem("goodstone_orders", JSON.stringify(ordersArray));
        if (typeof callback === "function") callback(ordersArray);
    });
}
