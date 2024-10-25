let checkedBoxes = [];
let addToCart = document.querySelector(".addToCartText");

let addToCartButton = document.querySelector(".cart_button");
let originalDisplay = addToCartButton.style.display;
let originalText = addToCart.textContent;

let priceTag = document.querySelector(".priceTag");

function checkStock() {
  if (
    checkedBoxes.length > 0 &&
    (parseFloat(checkedBoxes[checkedBoxes.length - 1].name) == 5.5 ||
      parseFloat(checkedBoxes[checkedBoxes.length - 1].name) == 7)
  ) {
    addToCart.textContent = "OUT OF STOCK";
    addToCartButton.style = "background-color:gray";
    addToCartButton.disabled = true;
  } else if (
    checkedBoxes.length === 0 ||
    checkedBoxes[checkedBoxes.length - 1] ===
      checkedBoxes[checkedBoxes.length - 2]
  ) {
    addToCartButton.style = "background-color:gray";
    addToCartButton.disabled = true;
    addToCart.textContent = originalText;
  } else {
    addToCartButton.disabled = false;
    addToCartButton.style = originalDisplay; // Reset to original style
    addToCart.textContent = originalText;
  }
  if (checkedBoxes.length > 0) {
    if (parseFloat(checkedBoxes[checkedBoxes.length - 1].name) == 3) {
      priceTag.textContent = "£110.00";
    } else {
      priceTag.textContent = "£130.00";
    }
  }
}

checkedBoxes = [];
check = 0;
function onlyOne(checkbox) {
  const checkboxes = document.querySelectorAll('input[type="checkbox"]');
  checkboxes.forEach((item) => {
    if (item !== checkbox) {
      item.checked = false;
    }

    if (item === checkbox) {
      document.querySelector("title").text =
        "ON Women's Cloud 5 Mesh Running Trainers - Size " + item.name;
      checkedBoxes.push(checkbox);
      check += 1;
    }
  });

  checkStock();
}

let count = 0;
if (count === 0) {
  let quantityIcon = document.getElementsByClassName("cartQuantity")[0];
  if (quantityIcon) {
    quantityIcon.style.display = "none";
  }

  addToCartButton.disabled = true;
  addToCartButton.style = "background-color:gray";
}

// Get the quantity icon and update its display and text content
function add_to_cart(element) {
  count += 1;

  let quantityIcon = document.querySelector(".cartQuantity");
  if (quantityIcon) {
    quantityIcon.style.display = "block";
    quantityIcon.textContent = count;
  }
}

function handleImageClick(pic) {
  mainPic = document.querySelector(".mainPic");

  let mainPicOldSource = mainPic.src;
  let oldPictureSource = pic.src;

  mainPic.src = oldPictureSource;
  pic.src = mainPicOldSource;
}

num = 0;
function addToWishlist(pic) {
  if (num % 2 == 0) {
    pic.src = "http://127.0.0.1:5501/svgs/filled_red_heart.png";
    pic.style = "width:26px";
    pic.style = "height:26px";
  } else {
    pic.src = "http://127.0.0.1:5501/svgs/heart.svg";
  }
  num += 1;
}

const pageTitle = document.querySelector(".product_name").textContent;
document.querySelector(".reviewsTitle").textContent = pageTitle;

let reviews = 0;
function submit(review) {
  const input1 = document.getElementById("usernameText").value;
  const input2 = document.getElementById("reviewInputText").value;
  if (input1.length > 0 && input2.length > 0) {
    const horizontalLine = document.createElement("div");
    horizontalLine.classList.add("horizontal-line");

    const parent = document.getElementById("reviewsTitleBlockID");
    const username = document.createElement("span");
    const reviewText = document.createElement("span");

    username.textContent = input1;
    reviewText.textContent = input2;
    parent.appendChild(horizontalLine);
    parent.appendChild(username);
    parent.appendChild(reviewText);
    parent.appendChild(horizontalLine);

    reviews += 1;
    document.querySelector(".reviewsCount").textContent = "Reviews :" + reviews;
  }
}
