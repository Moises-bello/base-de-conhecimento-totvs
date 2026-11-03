---
article_id: 360025512312
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: ff4b33aa2ebeb0b1e4c07b9c9cdbd8d28e4c8df3bd204e154f4549fcbb7975ee
fetched_at: '2026-06-28T22:37:55.354628+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CNAB - HELP NOBCOCAD
  Problema: Banco não cadastrado no arquivo de comunicação remota (SEE)'
type: support-article
updated_at: '2022-06-24T00:55:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025512312-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CNAB-HELP-NOBCOCAD-Problema-Banco-n%C3%A3o-cadastrado-no-arquivo-de-comunica%C3%A7%C3%A3o-remota-SEE
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:05:00min  
  
Ocorrência**No módulo Financeiro, ao tentar emitir o relatório retorno CNAB (**FINR650**) apresenta o Help: **NOBCOCAD Problema: Banco não cadastrado no arquivo de comunicação remota(SEE)**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - CNAB - Todas as versões  
  
**Causa**Esse incidente ocorre, pois a parametrização definida nas perguntas: **Banco**, **Agência**, **Conta** e **Sub Conta** do relatório retorno CNAB (**FINR650**) não está preenchido de acordo com o cadastro **Parâmetros Bancos**, como não encontra o registro na **SEE** que foi preenchido nas perguntas do relatório, é apresentado este Help.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Verifique se o tamanho das perguntas: **Banco**, **Agência**, **Conta** e **Sub Conta** do grupo de pergunta: **FINR650** está com o mesmo tamanho da **SX3** da tabela **SEE** dos campos: **Banco**, **Agência** e **Conta**, **Sub Conta**;  
2. Certo que não existe o campo **dígito** nas perguntas do relatório **FINR650**  assim como o cadastro **Parâmetros Bancos**. Verifique se o dígito consta no campo **Conta** no cadastro **Parâmetros Bancos**;
