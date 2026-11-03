---
content_hash: edd5225d2da18d7217f560ff112ce429e8466f5c1691f7273e6dfcc56a271f49
fetched_at: '2026-06-29T00:09:21.059485+00:00'
page_id: '422545784'
product: rm
source: tdn-rm
title: Parâmetros do Processo da NFS-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545784
version: 16
---

## **Conteúdo**

**Conteúdo**

## **01. Introdução**

Para o correto funcionamento do processo da NFS-e os parâmetros devem ser preenchidos previamente.  
Eles são encontrados no menu TOTVS Gestão de Estoque, Compras e Faturamento no item 04.03 - Integrações | 04.03.03 - Fiscal | 04.03.03.01 - Dados Fiscais.

## **02. Parâmetros Gerais**

**Definições Fiscais:** Neste parâmetro é possível definir a máscara do NCM e optar por vincular mensagens cadastradas no anexo da natureza de operação ao movimento.

Imagem

**Classificação IBGE Municípios:** Este parâmetro será utilizado para gerar o código dos municípios do Prestador, do Tomador e quaisquer outros códigos de municípios constantes no XML/TXT da NFS-e. Esta tabela é proveniente do IBGE. Esta classificação deve ser criada, preenchida e associada manualmente no cadastro de municípios. Os códigos de municípios podem ser consultados no portal [Cidades@ do IBGE](https://www.ibge.gov.br/geociencias-novoportal/organizacao-do-territorio/estrutura-territorial/15761-areas-dos-municipios.html?=&t=destaques). A incorreta classificação dos municípios acarretará na rejeição das NFS-e.

**Classificação Pais BACEN:**Este parâmetro será utilizado para gerar o código dos países envolvidos no processo da NFS-e. Esta Tabela de Países é proveniente do [Banco Central do Brasil (BANCEN)](http://www.bcb.gov.br/pt-br/paginas/default). Esta tabela deve ser criada, preenchida e associada manualmente no cadastro de países. A incorreta classificação dos países acarretará na rejeição das NFS-e.

**Configurações de Proxy Server:**Este parâmetro só deverá ser preenchido se o processo da NFS-e estiver integrado com o TSS.  Quando a integração é feita com o TOTVS Colaboração 2.0 a liberação do cliente deve ser feita diretamente no proxy/firewall pelo administrador da rede.   
Estas informações são fornecidas pelo administrador da rede. Se não houver necessidade de autenticação no proxy/firewall deixe estes parâmetros em branco.

**TOTVS Colaboração:** Informe aqui se o RM irá integrar o processo da NFS-e com o TOTVS Colaboração e em qual versão. Se a integração for esta basta preencher o diretório no qual o TOTVS Colaboração irá buscar os arquivos gerados pelo RM e gravar os arquivos baixados por ele. Se a integração for com o TSS escolha a opção Não Utiliza.   
Para maiores informações a respeito da implantação, instalação e configuração do TOTVS Colaboração 2.0 procure seu Gerente/Consultor de Implantação.

## **03. Parâmetros Por Filial**

**Conexão NF-e:** Neste parâmetro que efetivamente deve ser informado se o RM integra o processo da NFS-e com o TSS.  
  
    **URL do Servidor TOTVS Services:** Aqui deve ser informado a URL gerada para o TSS, exemplo: [http://SERVIDORXXX:8080](http://SERVIDORXXX:8080+)  
**Onde SERVIDORXXX** é o local onde o TSS está instalado.  
**Onde** **8080** é a porta reservada para a comunicação do TSS

**Autenticação TSS:** Campos Client Id TSS e Client Secret TSS: Informado de acordo com a exigência de cada prefeitura.

**NFS-e Municipal (Modelo Nacional)  
Versão do Layout da NFS-e utilizado:** Informe o layout atual do XML da Nota Fiscal de Serviço Eletrônica.  
Os campos **login da Prefeitura**, **Senha da Prefeitura** e **Autorização da Prefeitura** só devem ser preenchidos se a prefeitura da cidade na qual a filial está localizada, e para a qual envia as NFS-e, exige autenticação.   
 **NFS-e Municipal (Modelo Nacional)  
Ambiente NF-e:** Informe se a filial está operando em ambiente de Homologação (testes) ou Produção (nesta modalidade as notas possuem validade jurídica e fiscal).

Imagem

**Retirar Acentuações:** [Tratamento para Caracteres Especiais e Acentuações](https://tdn.totvs.com/x/ROHHPw)

**Texto para sanitização do Doc-e:** [Tratamento para Caracteres Especiais e Acentuações](https://tdn.totvs.com/x/ROHHPw)

**Número Máximo de NFS-e por lote:** Algumas prefeituras limitam o número de notas eletrônicas no lote de envio e se forem enviadas mais notas que o número permitido este lote é rejeitado. Se for deixado o valor 0 (zero) por default serão enviadas 50 notas. Aconselha-se utilizar o valor 10 (dez).  
**Classificação de Municípios:** Informe qual a classificação de municípios a prefeitura solicita no XML de suas NFS-e.  
**CNPJ Assinatura Lote NFS-e:** O CNPJ informado neste campo será utilizado para assinar o lote da NFS-e. Deve ser preenchido de acordo com a exigência da prefeitura para  a qual a NFS-e está sendo enviada.   
 **Certificação Digital 1/2:**Quando o processo da NFS-e é integrado com o TSS é necessário o uso do Certificado Digital A1. Escolha o tipo de certificado e informe os parâmetros de localização e a senha.  
Caso a prefeitura não utilize certificado é necessário preencher este campo com a opção "Nenhum" conforme imagem abaixo:

Imagem
