---
content_hash: 9b97a1ab5315a017ce76bebcbcc2192c02063fbd967fdfa2d79fb5f5c42979aa
fetched_at: '2026-06-29T00:09:21.065440+00:00'
page_id: '422545787'
product: rm
source: tdn-rm
title: Parâmetros do Processo de NFC-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545787
version: 6
---

Para o correto funcionamento do processo da NFC-e os parâmetros devem ter sido previamente preenchidos.   
 Eles são encontrados no TOTVS Gestão de Estoque, Compras e Faturamento no item 04.03 - Integrações | 04.03.03 - Fiscal | 04.03.03.01 - Dados Fiscais.

**Classificação IBGE Municípios:** Este parâmetro será utilizado para gerar o código dos municípios do Emitente, Destinatário, Transportadora e quaisquer outros códigos de municípios constantes no XML da NFC-e. Esta tabela é proveniente do IBGE. Esta classificação deve ser criada, preenchida e associada manualmente no cadastro de municípios. Os códigos de municípios podem ser consultados no portal Cidades@ do IBGE. A incorreta classificação dos municípios acarretará na rejeição das NFC-e.

**Classificação Pais BACEN:** Este parâmetro será utilizado para gerar o código dos países envolvidos no processo da NFC-e. Esta Tabela de Países é proveniente do Banco Central do Brasil (BANCEN). Esta tabela deve ser criada, preenchida e associada manualmente no cadastro de países. A incorreta classificação dos países acarretará na rejeição das NFC-e.

**Configurações de Proxy Server:** Este parâmetro só deverá ser preenchido se o processo da NFC-e estiver integrado com o TSS.  Quando a integração é feita com o TOTVS Colaboração 2.0 a liberação do cliente deve ser feita diretamente no proxy/firewall pelo administrador da rede.  
 Estas informações são fornecidas pelo administrador da rede. Se não houver necessidade de autenticação no proxy/firewall deixe estes parâmetros em branco.

**Parâmetros por Filial**

**Conexão NF-e:** É neste parâmetro que efetivamente é informado se o RM integra o processo da NFC-e com o TSS.  
                             URL do Servidor TOTVS Services: Aqui deve ser informado a URL gerada para o TSS.                                                 
                              Ex.: <http://SERVIDORXXX:8080>  
                              Onde SERVIDORXXX é o local onde o TSS está instalado.  
                                      8080 é a porta reservada para a comunicação do TSS  
    
                              NF-e Estadual  
                              Versão: Escolha a versão atual do layout da NF-e. A escolha de um layout desatualizada implicará na geração incorreta das informações da NF-e com consequente rejeição da mesma.  
    
                              NFS-e Municipal (Modelo Nacional)  
                              Versão do Layout da NFS-e utilizado: Informe o layout atual do XML da Nota Fiscal de Serviço Eletrônica.  
                              Os campos Login da Prefeitura, Senha da Prefeitura e Autorização da Prefeitura só devem ser preenchidos de a prefeitura da cidade na qual a filial está localizada e para a qual envia as NFS-e exige autenticação.

**Certificação Digital 1/2:** Quando o processo da NF-e é integrado com o TSS é necessário o uso Certificado Digital A1

                                             Escolha o tipo de certificado e informe os parâmetros de localização e a senha.  
           **Ambiente NFC-e:** Informações sobre o ambiente de operação da NFC-e.   
                                Ambiente de Envio: Informe se a filial está operando em ambiente de Homologação (testes) ou Produção (nesta modalidade as notas possuem validade jurídica e fiscal).  
                               Modalidade de Operação: Aqui é definido se a filial está trabalhando em modo normal ou em contingência. Este parâmetro pode ser alterado pelo processo de alteração de modalidade nos processos da NF-e/NFC-e.  
                               Versão do Layout NFC-e: Informe a versão do layout vigente de acordo com informado no site da Receita SEFAZ.  
                               O grupo Segurança será dividido em quatro informações que será utilizado para a criação do código QR Code e estes dados serão fornecido pela SEFAZ do estado:

* URL do QR Code
* URLda SEFAZ para Consulta da NFC-e
* Código de Segurança
* ID do Código de Segurança

Codificação de Pais e IBGE

* [Código BACEN](https://www.bcb.gov.br/rex/censo2000/port/manual/pais.asp?idpai=censo2000inf)
* [Portal IBGE](https://www.ibge.gov.br/geociencias-novoportal/organizacao-do-territorio/estrutura-territorial/15761-areas-dos-municipios.html?&t=destaques)
