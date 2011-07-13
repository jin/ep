#!/bin/bash
curl -H "Content-Type: text/xml" -d "<?xml version='1.0' encoding='utf-8'?><node><reading>300</reading></node>" http://localhost:8000/live/1/5/
