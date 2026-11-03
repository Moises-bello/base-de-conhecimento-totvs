---
article_id: 360051381394
category: RH - Relatórios Cadastros/Funcionários
content_hash: 894251a0e5b6b680722db05128f592efffea5fa4f7a7a16cde1e8868d68bc6d4
fetched_at: '2026-06-28T22:43:18.609213+00:00'
product: protheus
section_id: 360010843654
source: central-protheus
title: RH - Linha Protheus - GPE - Rotina para ajustar base histórica da ficha financeira
  (Updrdsrd)
type: support-article
updated_at: '2025-07-29T12:28:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051381394-RH-Linha-Protheus-GPE-Rotina-para-ajustar-base-hist%C3%B3rica-da-ficha-financeira-Updrdsrd
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33789047452823) Tempo aproximado para leitura: **00:01:00 min**  
**Ocorrência**Rotina para ajustar base histórica da ficha financeira (Updrdsrd).  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12  
  
**Causa**Sistema não envia dados de funcionário quando realizada transferência entre empresas duas vezes (T1 para T2 e retornando para T1), impedindo exibir histórico correto do demonstrativo de médias e ficha financeira.  
  
**Solução**

Para solucionar essa inconsistência de dados anteriores a correção da rotina **Transferência**, foi implementado o **RDMAKE Updrdsrd**. Sua finalidade é enviar dados da empresa origem para empresa destino que não foram no momento da transferência.

Essa rotina atualiza os dados referente ao Histórico de Movimentos - **SRD** da seguinte forma: serão enviados dados para a empresa destino somente para os casos que se caracterizam em transferência entre empresas, houve troca de matrícula e quando a empresa destino é uma empresa origem no histórico da **SRE**.

Para solucionar o problema na rotina de transferência foi realizado ajuste no fonte da rotina de transferência. Portanto, para as novas transferências que possuírem em histórico a empresa destino, todos os dados serão enviados para a nova empresa.   
Possibilitando que a geração do demonstrativo de médias na empresa atual seja exibido completamente.

Referente ao chamado [DRHGCH-13145 DT Demonstrativo de médias não traz histórico completo para funcionários transferido entre empresas](https://tdn.totvs.com/pages/viewpage.action?pageId=512433801).
