---
content_hash: ef3df8bdc281c2b3534a17f1ae0e724bf6bf7e83c249ea7202d372267fd3e7ca
fetched_at: '2026-06-29T00:09:07.718273+00:00'
page_id: '384588892'
product: rm
source: tdn-rm
title: Estrutura do XML S-1200 para pagamentos de dissídio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=384588892
version: 7
---

Segundo o MOS v.2.4.02 No caso de pagamento de diferenças salariais decorrentes de acordo coletivo de trabalho, convenção coletiva de trabalho ou de lei, o empregador deve utilizar o grupo [InfoPerAnt] e, se for o caso, informar a alteração contratual correspondente, conforme exemplo constante no evento “S-2206 – Alteração de Contrato de Trabalho”.

A estrutura do XML para informação de rubricas, é divida em duas partes:

**infoPerApur:**Destinado a informação de remuneração no período de apuração.

**infoPerAnt:** Destinado ao registro de:

a) remuneração relativa a diferenças salariais provenientes de acordos coletivos, convenção coletiva e dissídio;  
 b) remuneração relativa a diferenças de vencimento provenientes de disposições legais (órgãos públicos);  
 c) bases de cálculo para efeitos de apuração de FGTS resultantes de conversão de licença saúde em acidente de trabalho;  
 d) verbas de natureza salarial ou não salarial devidas após o desligamento.

**Condições no sistema:**

* Caso efetuar pagamento de Folha e Diferença Salarial por Dissídio no mesmo período de apuração, os dois grupos serão levados no S-1200;
* Caso efetuar apenas o pagamento de Diferença Salarial por Dissídio será levado apenas o grupo infoPerAnt. Essa situação pode ocorrer em casos que o funcionário não tem pagamento de folha naquela competência;
* Para o grupo infoPerAnt, serão levados os dados que foram lançados na ficha financeira (aba "Verbas geradas por diferenças" - PFVERBASDIS), através do processo de "Diferença Salarial" por "Dissídio". Isso é necessário pois o lançamento da diferença é feito de forma acumulativa no envelope, e o eSocial necessita dos valores relacionados em cada período de apuração anterior;

**Obs.:** Os eventos gerados no envelope relativos à Diferença Salarial por Dissídio não serão levados em nenhum grupo. Isso porque seus valores já foram levados através das "Verbas geradas por diferenças" no grupo infoPerAnt;

**Dissídios para Demitidos:**

* Se a diferença salarial referente a dissídio for lançada no mês da rescisão, o sistema levará para o evento S-2299 o grupo infoPerAnt conforme as descrições acima.
* Se a diferença salarial referente a dissídio for lançada por meio do cálculo de "Diferença Salarial" e/ou "Rescisão Complementar" em períodos de apuração após a rescisão, deverá ser gerado um evento S-1200. Nesse evento será levado apenas as informações do grupo infoPerAnt.
