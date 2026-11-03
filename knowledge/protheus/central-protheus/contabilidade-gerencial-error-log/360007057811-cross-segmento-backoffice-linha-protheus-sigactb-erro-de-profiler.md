---
article_id: 360007057811
category: Contabilidade Gerencial - Error log
content_hash: d21aaca0b33070002c69c40ddb4dfb5e31aac7bf8fb9121e3f9218fec915975f
fetched_at: '2026-06-28T22:40:52.000513+00:00'
product: protheus
section_id: 1500001537581
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ERRO DE PROFILER
type: support-article
updated_at: '2022-04-18T19:11:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007057811-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ERRO-DE-PROFILER
---

**Dúvida**  
Usuário sem permissão, erro de profiler

**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.

**Solução**

Realize o procedimento de manutenção de profiler.   
  
Realize primeiramente em ambiente de teste ou homologação para validação.  
  
Manutenção do profile de usuário siga os passos:  
  
1. Acesse o Configurador (SIGACFG);  
2. Acesse Usuários > Senhas > Usuários;  
3. Localize o Usuário, que deseja realizar a manutenção de profile;  
4. Anote o "Id do Usuário";  
5. Realize o Backup frio do diretório profile (frio = cópia com todos os serviços parados).  
6. Acessar SIGACFG;  
7. Acesse Ambiente > Cadastros > Manutenção Profile (Programa - PROFMGR);  
8. Localize todos os registros que estaja como o mesmo "Id do Usuário" na coluna "Usuário";  
9. Apagar pontualmente os registros do usuário onde ocorre o problema Ex: (CTBR040) e as demais rotinas.

Caso o erro persista, por favor entrar em contato.
