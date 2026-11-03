---
article_id: 4416132819479
category: 'Aplicativo MNTNG '
content_hash: a22f25943d1f7ac8caa7cdb700b0886342c238f38e91431724e5edf99347684c
fetched_at: '2026-06-28T22:42:37.654064+00:00'
product: protheus
section_id: 360010992174
source: central-protheus
title: Manufatura - Linha Protheus - APP MNT - Configuração Leitura de QR Code e Código
  de Barras
type: support-article
updated_at: '2022-06-21T14:50:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416132819479-Manufatura-Linha-Protheus-APP-MNT-Configura%C3%A7%C3%A3o-Leitura-de-QR-Code-e-C%C3%B3digo-de-Barras
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:01:15 min** **Dúvida**Como faço para utilizar a leitura de **QR Code** no aplicativo **MNTNG**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Aplicativo MNTNG - Versão 12  
  
**Solução**Para utilizar o leitor de **QR COde** e leitor de **Código de barras**:

* O aplicativo **MntNG** deve ser atualizado para a versão **1.10.0**.
* O **Web Service MNTNG** também deve estar atualizado, em versão **2.5.0** ou superior.
* A funcionalidade foi desenvolvida para **Android 7.0 - API de nível 24** ou superior. A leitura do **QR Code** deve ser feita pela câmera traseira do dispositivo.
* Incluir pergunta **Tipo de Código** do grupo de perguntas **MNT601 - Em Base de Dados/Dicionário/Base de Dados/Perguntas**, selecionar o grupo **MNT601**, acionar a opção **Editar**, incluir a pergunta **Tipo de Código**.
* Incluir a função **MNTA080VLD** na validação no campo **Código de Barras - T9\_BARCODE** da tabela **ST9 - Bens**. Para isso, acesse no **SIGACFG -** **Base de Dados/Dicionário**, selecione a tabela **ST9**, vá na opção **Editar/Bem/Campos**. Selecionar o campo **T9\_BARCODE,** editar e adicionar a validação do campo conforme imagens disponíveis no *link* da seção **Saiba mais**.

**Saiba mais**Acesse a documentação completa no *link*: [Leitura de código de barras e QR Code no aplicativo MNT NG](https://tdn.totvs.com/pages/releaseview.action?pageId=654501795#1-2)
