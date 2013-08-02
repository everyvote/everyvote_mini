function handleSelect(constituency_form) {
    // display an alert box
    // containing the selected text
    // alert(constituency_form.constituency_selector.options.length)
    var selIndex = constituency_form.constituency_selector.selectedIndex;
    // alert(selIndex);
    
    var selName = constituency_form.constituency_selector.options[selIndex].id;
    alert(selName);
}

