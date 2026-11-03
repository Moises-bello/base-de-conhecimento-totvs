---
article_id: 360053211553
category: RH - Soluções para error.log
content_hash: 3b66887970a8ed35d5ab28ddb5722b7258fd2601c19d9931e4b829f5aaf1459d
fetched_at: '2026-06-28T22:44:08.891042+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: 'RH - Linha Protheus - GPE - Error log ao gerar Relatório Demonstrativo de
  Horas - argument #0 error, expected C->N,  function substr on R330IMP'
type: support-article
updated_at: '2025-08-05T14:32:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053211553-RH-Linha-Protheus-GPE-Error-log-ao-gerar-Relat%C3%B3rio-Demonstrativo-de-Horas-argument-0-error-expected-C-N-function-substr-on-R330IMP
---

**Ocorrência**  
Ao realizar a geração de Relatório Demonstrativo de Horas, através da rotina **GPER330**, é gerado ***error log**: **argument*****#0*****error, expected*** **C->N*****,  function substr on*** **R330IMP(GPER330.PRX)**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - a partir da versão 12.1.27  
  
**Causa**Este erro ocorre devido à inconsistência no grupo de perguntas  
  
**Solução  
1.** Para solucionar essa ocorrência, necessário acessar via Configurador, o Grupo de Perguntas **GPR330**:  
[MP - GPE - Como alterar o grupo de perguntas (SX1) pelo configurador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033213634-MP-GPE-Como-alterar-o-grupo-de-perguntas-SX1-pelo-configurador?source=search)  
  
**2.** Validar se as perguntas estão na mesma ordem e Tipo e Objeto conforme demonstrado no padrão deste Grupo de Perguntas, abaixo (abra a imagem em outra aba ou salve-a em seu computador para facilitar a visualização de cada item):  
![jfd7YmPpM5D0w4nDbxzUnZw0n (1919×750)](https://p23.zdusercontent.com/attachment/888110/jfd7YmPpM5D0w4nDbxzUnZw0n?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..de9fLgeOH0pPBO30EPRhvw.6AhI_Xh9T-Z8d7RwZbXj4x0j4H93dZdBhRDkjhGHzMJHWTkw4zKVfWMxkReUdf3_9804479WbZNTtFoHsiWH8C0ab-MiB5vP2WoklDZYWZW_0n9gged2wci_6X44qvwqNEffM34-BZT6UYNt06NYoBC1e6JuyF4t_53SDJEh3uvd6ZAhmmPIrMtu8vFsv_ZC2HSy_-IOof-QdPRmaSpeZU2qD_888ZXl4scoOWd0wIJGlQpJ4YXtmDjvIgKezx4GVhqKJQaqz9qcYQmkVRvDoldUvuqq1TaMFs1bh42-93E.uVOsjRdGWCzYNBH-S77XIQ)  
  
**3.** Ajustar quaisquer divergências que houverem em seu ambiente neste Grupo de Perguntas.  
  
**Saiba mais:**  
[Pacote Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Soluções para error log](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115003853987-RH-Solu%C3%A7%C3%B5es-para-error-log)
