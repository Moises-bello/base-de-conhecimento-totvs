---
content_hash: 687c9ed2d87fdc428016f13ad9f546b73ae2f95bd2acfa392927e6337b9a9c9c
fetched_at: '2026-06-29T00:09:24.002142+00:00'
page_id: '422546185'
product: rm
source: tdn-rm
title: Parâmetros do Processo da NF-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546185
version: 2
---

Para o correto funcionamento do processo da NF-e os parâmetros devem ter sido previamente preenchidos.  
 Eles são encontrados no TOTVS Gestão de Estoque, Compras e Faturamento no item 04.03 - Integrações | 04.03.03 - Fiscal | 04.03.03.01 - Dados Fiscais.

**Classificação IBGE Municípios:** Este parâmetro será utilizado para gerar o código dos municípios do Emitente, Destinatário, Transportadora e quaisquer outros códigos de municípios constantes no XML da NF-e. Esta tabela é proveniente do IBGE. Esta classificação deve ser criada, preenchida e associada manualmente no cadastro de municípios. Os códigos de municípios podem ser consultados no portal Cidades@ do IBGE. A incorreta classificação dos municípios acarretará na rejeição das NF-e.

**Classificação Pais BACEN:** Este parâmetro será utilizado para gerar o código dos países envolvidos no processo da NF-e, principalmente quando se tratar de notas de Importação/Exportação de mercadorias. Esta Tabela de Países é proveniente do Banco Central do Brasil (BANCEN). Esta tabela deve ser criada, preenchida e associada manualmente no cadastro de países. A incorreta classificação dos países acarretará na rejeição das NF-e.

**Configurações de Proxy Server:** Este parâmetro só deverá ser preenchido se o processo da NF-e estiver integrado com o TSS.  Quando a integração é feita com o TOTVS Colaboração 2.0 a liberação do cliente deve ser feita diretamente no proxy/firewall pelo administrador da rede.  
 Estas informações são fornecidas pelo administrador da rede. Se não houver necessidade de autenticação no proxy/firewall deixe estes parâmetros em branco.

**TOTVS Colaboração:** Informe aqui se o RM irá integrar o processo da NF-e com o TOTVS Colaboração e em qual versão.Se a integração for esta basta preencher o diretório no qual o TOTVS Colaboração irá buscar os arquivos gerados pelo RM e gravar os arquivos baixados por ele. Se a integração for com o TSS escolha a opção Não Utiliza.   
 Para maiores informações a respeito da implantação, instalação e configuração do TOTVS Colaboração 2.0 procure seu Gerente/Consultor de Implantação.

**Parâmetros por Filial**  
    
 **Conexão NF-e:** É neste parâmetro que efetivamente é informado se o RM integra o processo da NF-e com o TSS.  
                              URL do Servidor TOTVS Services: Aqui deve ser informado a URL gerada para o TSS.                                                 
                              Ex.: <http://SERVIDORXXX:8080>  
                              Onde SERVIDORXXX é o local onde o TSS está instalado.  
                                      8080 é a porta reservada para a comunicação do TSS  
    
                              NF-e Estadual  
                              Versão: Escolha a versão atual do layout da NF-e. A escolha de um layout desatualizada implicará na geração incorreta das informações da NF-e com consequente rejeição da mesma.  
    
                              NFS-e Municipal (Modelo Nacional)  
                              Versão do Layout da NFS-e utilizado: Informe o layout atual do XML da Nota Fiscal de Serviço Eletrônica.  
                              Os campos Login da Prefeitura, Senha da Prefeitura e Autorização da Prefeitura só devem ser preenchidos de a prefeitura da cidade na qual a filial está localizada e para a qual envia as NFS-e exige autenticação.        
    
    **Ambiente NF-e:** Informações sobre o ambiente de operação da NF-e.  
                               NF-e Estadual  
                               Ambiente de Envio: Informe se a filial está operando em ambiente de Homologação (testes) ou Produção (nesta modalidade as notas possuem validade jurídica e fiscal).  
                               Modalidade de Operação: Aqui é definido se a filial está trabalhando em modo normal ou em alguma contingência. Este parâmetro pode ser alterado pelo processo de alteração de modalidade nos processos da NF-e.  
 Tempo de Espera para entrar em contingência: É o tempo expresso em minutos para o processo de envio da NF-e  ser executado sem sucesso até que seja sugerida a entrada em contingência. Aconselhamos o uso do valor 0 (zero) para que o processo seja executado até o tempo default do ambiente da SEFAZ. Se o usuário gravar um tempo muito pequeno corre-se o riso do sistema sugerir a entrada em contingência desnecessariamente.   
    
  NFS-e Municipal (Modelo Nacional)  
                                Ambiente de Envio: Informe se a filial está operando em ambiente de Homologação (testes) ou Produção (nesta modalidade as notas possuem validade jurídica e fiscal).  
                                Número Máximo de NFS-e por lote: Algumas prefeituras limitam o número de notas eletrônicas no lote de envio e se forem enviadas mais notas que o número permitido este lote é rejeitado. Se for deixado o valor 0 (zero) por default serão enviadas 50 notas. Aconselha-se utilizar o valor 10 (dez).  
                                Classificação de Municípios: Informe qual a classificação de municípios a prefeitura solicita no XML de suas NFS-e.  
    
 **Certificação Digital 1/2:** Quando o processo da NF-e é integrado com o TSS é necessário o uso Certificado Digital A1  
                                              Escolha o tipo de certificado e informe os parâmetros de localização e a senha.  
    
           **Ambiente CC-e:** Parâmetros do ambiente da Carta de Correção Eletrônica.  
                                Identificação do ambiente: Informe se a filial está trabalhando em ambiente de Homologação ou Produção.  
                                Identificação de Horário de Verão: Informar se a Filial está em período de horário de verão.  
                                Identificação do Horário: Informa em qual horário a filial está baseando seu horário de tempo.  
                                Informe as versões atualizadas de Layout, Layout do evento, Versão do evento e versão da carta de correção.
