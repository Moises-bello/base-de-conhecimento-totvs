---
article_id: 360006655452
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: a8cbd055cb95da6384c99076bd037889e6976dad7ffb8523bea2c225b921f6b4
fetched_at: '2026-06-28T22:40:32.379315+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB- Pacote Acumulado contabilidade
  gerencial e procedimentos para atualização.
type: support-article
updated_at: '2021-08-31T18:55:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006655452-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Pacote-Acumulado-contabilidade-gerencial-e-procedimentos-para-atualiza%C3%A7%C3%A3o
---

**Dúvida**  
Pacote Acumulado da contabilidade gerencial e procedimentos para atualização.

**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial- a partir da versão 12

**Solução**

**1- [Pacotes de Atualização - Contabilidade](https://tdn.totvs.com/pages/releaseview.action?pageId=334342777)**

Através deste canal, disponibilizamos os principais pacotes de atualização e correção do produto Protheus Contabilidade Gerencial, para serem baixados via download.

Este trabalho é realizado especificamente para casos críticos que envolvam alto volume de atendimento. Todos estes pacotes são oficiais e homologados pelo time TOTVS, como normalmente disponibilizado por meio da Central de Downloads (Portal do Cliente).

Os pacotes contidos nesta página ficarão disponíveis até a próxima liberação do repositório de dados no portal do cliente. Após esta liberação os pacotes de atualização serão removidos da página.

**2-** Baixando o Pacote via Portal do cliente:

Atualizar ambiente com  últimos pacotes disponíveis no portal

Verificar possibilidade de realizar  em ambiente teste os procedimentos que seguem, e se ainda apresenta ocorrência

 Em ambiente de homologação,

* Acessar o portal do cliente e realize o download do ultimo dicionário completo e diferencial disponibilizado.

Ex.:

* DICIONARIOS\_COMPL\_12\_1\_17 - Completo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015159831/mceclip0.png)

* DICIONARIOS\_DIF\_12\_1\_17 - Diferencial

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015159891/mceclip1.png)

Obs.: Lembrando que em caso de dicionários para outros países, deve-se realizar o download do pais respectivo, aplicando sempre o mais atualizado.

Obs.: Lembrando que em caso de dicionários para outros países, deve-se realizar o download do pais respectivo.

1. Realize o download do ultimo pacote "GERAL ACUMULADO" do Protheus, contendo todas as correções liberadas.
2. Realizar o backup do seu ambiente (dicionário, RPO e dados)

2. Excluir os arquivos de log abaixo:

Dentro da pasta system:

mpupdlog.log  
mpupdlog.fpt  
mpwizard.hlp  
mpwizardhlp.lck

Dentro da pasta Appserver:

mpupddistri.tsk

4. Copiar os arquivos do dicionário para a sua pasta **systemload**
5. Aplicar o pacote "GERAL ACUMULADO" em seu ambiente.
6. Realizar a execução do **UPDDISTR do acumulado e diferencial. (sem a execução deste processo o erro não e corrigido)**

**Veja mais**

Links com esclarecimento para atualização do ambiente e do portal

<http://tdn.totvs.com/pages/viewpage.action?pageId=201727445>

<https://suporte.totvs.com/portal/p/10098/download#000006/P12117/>
