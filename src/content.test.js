import test from 'node:test';
import assert from 'node:assert/strict';
import { themes, searchContent } from './content.js';
import { readFileSync } from 'node:fs';
test('alle zes thema’s zijn uniek en hebben volledige detailinhoud',()=>{assert.equal(themes.length,6);assert.equal(new Set(themes.map(t=>t.slug)).size,6);for(const t of themes){assert.ok(t.body);assert.equal(t.actions.length,3);}});
test('zoeken vindt thema’s, pagina’s en woorden uit de detailinhoud',()=>{assert.ok(searchContent(' INTEGRITEIT ').some(r=>r.href==='#/handreiking/integriteit'));assert.ok(searchContent('nulmeting').some(r=>r.href==='#/handreiking'));assert.ok(searchContent('toegangsrechten').some(r=>r.href==='#/handreiking/informatie'));assert.ok(searchContent('intimidatie').some(r=>r.href==='#/handreiking/publieke-taak'));assert.deepEqual(searchContent(''),[]);assert.deepEqual(searchContent('onvindbarezoekterm'),[]);});
test('de download bevat elk thema en velden voor beoordeling en opvolging',()=>{const csv=readFileSync(new URL('../public/werkchecklist.csv',import.meta.url),'utf8');for(const t of themes)assert.ok(csv.includes(t.name));for(const field of ['Status','Prioriteit','Verantwoordelijke','Termijn'])assert.ok(csv.includes(field));});
