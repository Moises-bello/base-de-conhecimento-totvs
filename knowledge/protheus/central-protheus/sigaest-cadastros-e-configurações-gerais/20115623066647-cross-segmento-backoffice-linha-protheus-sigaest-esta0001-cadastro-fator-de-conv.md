---
article_id: 20115623066647
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 1726a7d10ab841cb9a25e0923bea7f2c46eb1a7ce749d68bb30dc84c5cad15fe
fetched_at: '2026-06-28T22:39:08.239833+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - ESTA0001 - Cadastro
  Fator de Conversão Unidade de Medida
type: support-article
updated_at: '2025-03-12T12:23:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20115623066647-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-ESTA0001-Cadastro-Fator-de-Convers%C3%A3o-Unidade-de-Medida
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20115616892055) Tempo aproximado para leitura: **00:04:40 min** **Dúvida**Como configurar e utilizar o ESTA0001 - Cadastro Fator de Conversão Unidade de Medida?  
  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**A rotina Fator de Conversão de Unidade de Medida tem lançamento programado para o **Microsiga Protheus® Release 12.1.2310**, porém é possível realizar a implantação em releases anteriores atualizando rotinas e dicionário disponibilizados em nosso pacote acumulado do sistema a partir de 16/12/2022.

#### **Nova Regra de Validações EFD**

Para atender a resolução 0001/2022 - GSEFAZ, Decreto 43.281/2021, a SEFAZ AMAZONAS começou a validar os registros C100 e C170 na EFD ICMS IPI para Documentos de entrada sob a perspectiva do emissor do documento fiscal (XML).

Na escrituração dos itens de Nota Fiscal de Entrada, será verificado informações que constam no arquivo xml recebido do fornecedor.  
Sendo necessário que contenha a mesma sequência dos itens, descrição item/produto e unidade de medida.

A rotina de Cadastro Fator de Unidade de Medida auxilia neste processo registrando um fator de conversão para a Unidade de Medida Comercial, sendo possível assim receber um produto na unidade comercial enviada pelo fornecedor, porém registrar na unidade de estoque local uma unidade de medida diferente, cadastrando um fator de conversão para a mesma.

Importante ressaltar que o Cadastro Fator de Conversão Unidade de Medida é especificamente para os clientes que utilizam Consolidador XML (SEFAZ AM) ou Nota Fiscal Manual de Entrada (MATA910) disponibilizado pelo módulo de Compras.

**Pré Configurações/Requisitos**

Para acessar a rotina de **Fator de Conversão de Unidade de Medida**, é necessário seguir os seguintes requisitos:

* No dicionário de dados do ambiente, deve existir a tabela: Fator de Conversão UM (D3Q).

Caso apresente mensagem de alerta informando acerca da necessidade de atualização de dicionário ou fontes, recomendamos que o ambiente seja atualizado através do pacote de expedição contínua do módulo apresentado, através do link:

<https://tdn.totvs.com/pages/viewpage.action?pageId=522000602>

**Criação de item de Menu**  
Siga o passo a passo abaixo para implantação e utilização do Fator de Conversão de Unidade de Medida.

Adicione a rotina no Menu do módulo de Estoque(SIGAEST), seguindo os passos abaixo:

**1)** Acessar o SIGACFG;

**2)** Acessar a rotina Ambiente→ Cadastros→ Menus (CFGX013);

**3)** Selecionar o módulo de Estoque/Custos;

**4)** Selecionar a opção Novo Item informando a rotina ESTA0001;

**5)** Após a inclusão do menu, é possível acessar o módulo Estoque/Custos, navegar até a pasta selecionada para inclusão da rotina, e verificar os recursos disponíveis.

**Exemplo prático de inclusão de Menu**

![MenuUM.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/20115623061911)

**Demais informações e detalhes de como usar a rotina, acesse:**

<https://tdn.totvs.com/pages/viewpage.action?pageId=701678746>

**Saiba mais:**

*[Clique aqui para mais informações sobre a MATA010](https://tdn.totvs.com/display/public/PROT/Produtos+-+MATA010#ProdutosMATA010-PastaCadastrais)*

*[Clique aqui e veja mais artigos sobre Cadastros e Configurações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Configuração de numeração automática (B1\_COD) via LicenceServer](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406595504279-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Configura%C3%A7%C3%A3o-de-numera%C3%A7%C3%A3o-autom%C3%A1tica-B1-COD-via-LicenceServer)*

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Configuração de envio Messenger para ID de eventos do Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003963562-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Configura%C3%A7%C3%A3o-de-envio-Messenger-para-ID-de-eventos-do-Estoque)*
