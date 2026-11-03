---
content_hash: c371d47a484ddd1ffb1728ff296662067a2b7a57b7160a391f17a80cd60148a6
fetched_at: '2026-06-29T00:05:54.710910+00:00'
page_id: '1081151885'
product: rm
source: tdn-rm
title: Declaração de Conteúdo Eletrônica (DC-e)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1081151885
version: 11
---

![](https://tdn.totvs.com/download/attachments/1081151885/DC-e.png?version=1&modificationDate=1782410009789&api=v2)
]]>

# Conteúdo

**Conteúdonone**

# 1. Visão Geral

A **Declaração de Conteúdo Eletrônica (DC-e)** modelo 99 é um documento fiscal digital utilizado para registrar o transporte de bens e mercadorias que não exigem emissão de nota fiscal. Ela substitui a declaração em papel, garantindo maior segurança, rastreabilidade e controle das informações. Após a autorização, é gerada a **DACE**, representação gráfica que acompanha a mercadoria durante o transporte.

# 2. Parâmetros

Para emissão da DC-e é necessário configurar alguns parâmetros conforme abaixo.

ParametrosleftParâmetros Gerais

Parâmetros gerais para configuração da emissão da DC-e

falsefalseParametrizações GeraisConexão NF-e

**Conexão NF-e**

Em Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Integrações | Fiscal | Dados Fiscais | Parâmetros por Filial | <escolha a Filial que emitirá NFCom> | Conexão NF-e. Devem ser configurados os parâmetros **URL do Servidor TOTVS Service** e os **dados de Autenticação.**

Imagem

**#####imagem**

Dicas

Instalação do TSS: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/18590720143639>

Este passo deve ser configurado apenas quando a transmissão for realizada utilizando o TSS

Certificado Digital 1/2

**Certificado Digital**

Em Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Integrações | Fiscal | Dados Fiscais | Parâmetros por Filial | <escolha a Filial que emitirá NFCom> | Certificado Digital 1/2. Deve ser configurado o certificado Digital para emissão da NFCom

Imagem

**#####imagem**

Dicas

Como preparar o certificado digital: [NFE0006\_Preparar\_Certificado\_Digital](https://tdn.totvs.com/display/LRM/NFE0006_Preparar_Certificado_Digital)

Cadastro do certificado digital:

Este passo deve ser configurado apenas quando a transmissão for realizada utilizando o TSS

Ambiente DC-e

**Ambiente DC-e**

Em Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Integrações | Fiscal | Dados Fiscais | Parâmetros por Filial | <escolha a Filial que emitirá DC-e> | Ambiente DC-e.

Ambiente NFCom

**#####imagem**

Dicas

Consulte a URL do QRCode para o sua UF: <https://dfe-portal.svrs.rs.gov.br/Nfcom/Servicos>

Parâmetros do Movimento

Parâmetros do Tipo de Movimento para emissão da DC-e

Parametrizações Tipo MovimentoMov - Faturamento 1/6

* Mov - Faturamento 1/6:  O Tipo de Movimento deve gerar Faturamento, o grupo de fatura será obrigatório na DC-e.

  Imagem
Fis - Escrituração

* Fis - Escrituração 1/2: marcar o campo "Gerar Escrituração" e no campo "Tipo Documento Escrituração", selecionar tipo de documento cujo campo Código do Modelo do Documento = 99.

  Imagem

Dica

Cadastro do Tipo de Documento:

Fis - NF-e

* Fis - NF-e: Informar campo "DC-e" como Integrado.

  Imagem

## 3. Nota Fiscal de Comunicação Eletrônica (DC-e)

A tela da NFCom será acessada através do módulo Gestão de Estoque, Compras e Faturamento, no menu Vendas | Documentos Eletrônicos | Declaração de Conteúdo Eletrônica (DC-e).

Cada DC-e apresentará os dados de identificação da Declaração, o xml com todas as informações que compões o documento e um status da situação atual do documento.

## 3.1 Anexos

AnexosHistórico

No Anexo de Histórico, teremos um registro detalhado de cada alteração na DC-e principal. As informações exibidas serão idênticas às da Tela Principal, com a única diferença sendo o ID do histórico. Isso permitirá visualizar cada modificação feita na DC-e até a data atual. Além disso, será possível visualizar e baixar o XML correspondente a cada momento, funcionando como uma fotografia armazenada para cada alteração.

Aba Identificação

**#####imagem**

Aba XML

**#####imagem**

Eventos

No Anexo de Evento [(Clique Aqui)](https://tdn.totvs.com/display/LRM/Eventos+NFCom), teremos um registro detalhado de cada evento efetuado na DC-e principal. Armazenando e exibindo os status e datas de cada evento, juntamente com os XML de Envio e o XML de Retorno.

## 3.2 Processos

A DACE passará por algumas etapas até ser devidamente autorizada, abaixo segue um fluxo macro dessas etapas. Para compreender em detalhe o funcionamento de cada etapa, clique no processo desejado para ser direcionado à página do processo.

#0022331dashedLista dos Processos





* [Enviar Evento](https://tdn.totvs.com/display/LRM/Eventos+NFCom)
* [Consultar Evento](https://tdn.totvs.com/display/LRM/Eventos+NFCom)

# 4. Edição da DC-e

#002233dashed

## 4.1 Movimento: Edição, Cancelamento e Exclusão

As consistências são realizadas quando o tipo de movimento estiver parametrizado em: Etapa 67 - Fiscal - Nota Fiscal Eletrônica (Fis - NF-e), campo NFcom = Integrado.

Só é permitido Editar, cancelar ou excluir movimentos cujo o status da NFCom seja diferente de: Pendente, Autorizado, Cancelamento Pendente e Cancelado.

**Editar:** Ao editar um movimento, o status da NFCom é alterado para Editado.

**Cancelar:** Ao cancelar um movimento, a NFCom é excluída.

**Excluir:** Ao excluir um movimento, a NFCom é excluída.

#002233dashed

## 4.2 DC-e: Edição

Os registros da NFCom não devem ser editados diretamente e suas alterações devem ser realizadas pelos processos da NFCom. Entretanto, para situações adversas consulte a documentação:

# 5. DACE

O **DACE** é a representação gráfica simplificada da **DC-e**, impressa em papel comum e destinada ao consumidor de serviços de telecomunicações. Ele funciona como a conta mensal de consumo, permitindo a visualização resumida das informações fiscais e de cobrança.

Para detalhes técnicos e orientações completas sobre o DACE, consulte a documentação específica [clicando aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=990764154)

# 6. Atualizações e Notas Técnicas

# 7. Vídeos

noneWebinar EFD-Reinf

648432

# 8. Documentos Auxiliares

## 8.1 Instalação do TSS

A transmissão da NFCom para o ambiente da SEFAZ é realizada por meio do aplicativo **TSS**. Para orientações de instalação e configuração, consulte a documentação: [Instalação e atualização do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18590720143639)

## 8.2 Preparar o certificado

A emissão da NFCom requer o uso de um **certificado digital modelo A1**, que garante a autenticidade e a validade jurídica do documento. Para realizar a configuração do certificado, siga as instruções disponíveis em: [NFE0006\_Preparar\_Certificado\_Digital](https://tdn.totvs.com/display/LRM/NFE0006_Preparar_Certificado_Digital)

# Informações sobre LGPD

**Informamos que os dados pessoais contidos nesta entidade foram colhidos para emissão de documentos fiscais e geração de rotinas legais e são retidos por determinação legal de normas fiscais e de transparência. Os mesmos não poderão ser eliminados em virtude de obrigação legal de retenção. O cumprimento de obrigação legal é hipótese legítima do tratamento dos seus dados conforme a Lei Geral de Proteção de Dados Pessoais (Lei n° 13.709/2018).**

**Para mais informações sobre a LGPD e as soluções oferecidas pela TOTVS consulte nossa página neste link ([https://tdn.totvs.com/pages/releaseview.action?pageId=514427789](https://tdn.totvs.com/pages/releaseview.action?pageId=514427789 "Follow link")).**

Imagens
