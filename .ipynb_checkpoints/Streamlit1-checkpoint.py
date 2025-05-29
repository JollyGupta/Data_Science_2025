{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "33f6ecc7-8926-4136-aeba-d2291b489813",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-11-27 19:00:29.971 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\hp\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Save this as app.py\n",
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "# Title and Description\n",
    "st.title(\"Simple Streamlit App\")\n",
    "st.write(\"This is a basic example of using Streamlit.\")\n",
    "\n",
    "# DataFrame Display\n",
    "data = pd.DataFrame({\n",
    "    'Column A': [1, 2, 3, 4],\n",
    "    'Column B': [10, 20, 30, 40]\n",
    "})\n",
    "st.write(\"Here's a DataFrame:\", data)\n",
    "\n",
    "# Adding a Slider\n",
    "value = st.slider(\"Select a value\", min_value=0, max_value=100, value=50)\n",
    "st.write(f\"Selected value: {value}\")\n",
    "\n",
    "# Line Chart\n",
    "chart_data = pd.DataFrame(\n",
    "    np.random.randn(20, 3),\n",
    "    columns=['A', 'B', 'C']\n",
    ")\n",
    "st.line_chart(chart_data)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e4b70b5e-1a3d-4815-85b5-183f4230540e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fd9a4e5c-7f16-4e8d-bdbd-30148d84c9bb",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d87ed6e5-1eae-43ab-b6a3-618ed3c98f08",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "928579d0-2117-4680-a74e-5e8d5dae766d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5a885d6a-a73c-4ebe-85c6-c0b4f88eb09e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ee75cde7-2c7f-428b-a142-12fd78708764",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "32b11f9d-30e0-4ed0-9a1c-3e798ce11917",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ecae5124-6a23-4725-b8ba-473d2ec15623",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
