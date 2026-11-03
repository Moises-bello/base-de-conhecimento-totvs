---
content_hash: d77748c3546ea75a2098131cb20d2683972ba10b4a6bf43a63acb7fd9ef97d4a
fetched_at: '2026-06-29T00:11:28.251906+00:00'
page_id: '73073287'
product: rm
source: tdn-rm
title: RMPAT00011_Contabilização de Baixa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=73073287
version: 4
---

|  |  |  |
| --- | --- | --- |
| **Produto** | : | Totvs Gestão Patrimonial – **Versão:** 11.5x |
| **Processo** | : | Contabilização de Baixa |
| **Subprocesso** | : | Ocorrências |
| **Data da publicação** | : | 24/07/2013 |

**Introdução**

As Ocorrências de Baixa agora precisam ter sua contabilização gerada para posteriormente ser enviada para o RM Saldus. Abaixo segue instruções de como realizar o procedimento na nova plataforma Bonum.Net. 

**Desenvolvimento/Processo (Contabilização Baixa)**

**Disponível em:** Operações Patrimoniais / Consulta|Cancela / Ver Baixa Total

Deverão ser selecionadas as Linhas de ocorrências para a contabilização da Baixa.  
E após contabilizar: Processos / Contabilização / Baixa

 

Será apresentado o Patrimônio Baixado, e as demais informações são características para o lançamento contábil a ser gerado no TOTVS Gestão Contábil.

**Cenário(s) e Conferência:** Nesta etapa serão apresentados os cenários existentes dentro do Patrimônio, e no qual sofreram a baixa.  
No Exemplo abaixo existe o Cenário da moeda Real – R$ e o Cenário da moeda Dolar - US$.   
Clicando no botão **Contabilização**, será possível, conferir todos os dados do lançamento contábil a ser gerado.

   
A tela apresentada abaixo, já mostra exatamente como o Lançamento ficará no RM Saldus.  
É preciso ter atenção (conforme a seta indica) neste processo só estamos cadastrando a contabilização, ainda não estamos enviando para o Saldus. Caso tenha algum dado para ser ajustado (ex. centro de custo, departamento, filial, etc), poderá também ser feito nesta tela.

 **Concluindo a contabilização:** Avançar / Executar   
Nesta tela o Sistema te apresentará os dados se a contabilização foi efetuada.  
Verifique atentamente este Log.

   
Assim o Status da coluna 'Contabilização' será alterado para Contabilizado.

   
**Desenvolvimento/Processo (Integrar Contabilização de Baixa com Totvs Gestão Contábil)**

**Disponível em:** Contabilização / Integrar Contabilização

Automaticamente o sistema apresentará o Período de Contabilização vigente da competência.  
Deverá ser informado o Lote a ser criado dentro do Totvs Gestão Contábil para esta contabilização.  
Lembre-se que como estamos contabilizando a Baixa, devemos selecionar a **Operação:** Ocorrências.   
  
Para a certeza que a Contabilização foi integrada para o Totvs Gestão Contábil com Sucesso, verifique sempre no Bloco de Notas a mensagem completa verificando a quantidade de Operações que foram integradas.
