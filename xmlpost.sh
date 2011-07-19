#!/bin/bash
curl -H "Content-Type: text/xml" -d "<?xml version='1.0' encoding='utf-8'?><data><reading>300</reading><batt>50</batt><seq>50</seq><cluster>2</cluster><node>4</node></data>" http://192.168.1.4:8000/api/xml/clusters


