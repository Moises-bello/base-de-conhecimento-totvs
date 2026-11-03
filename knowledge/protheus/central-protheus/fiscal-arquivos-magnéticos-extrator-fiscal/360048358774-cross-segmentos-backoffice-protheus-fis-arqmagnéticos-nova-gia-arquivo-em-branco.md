---
article_id: 360048358774
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: d51854c0f8cbe43a8e14dbf119688da80fc773e3be9019487632ace9e5ca4e01
fetched_at: '2026-06-28T22:42:07.935827+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Nova GIA - Arquivo
  em Branco ou com Valores Incorretos.
type: support-article
updated_at: '2024-06-10T12:45:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048358774-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Nova-GIA-Arquivo-em-Branco-ou-com-Valores-Incorretos
---

**Dúvida**

Ao efetuar a geração do arquivo da Nova GIA, o arquivo está saindo em branco/somente com o cabeçalho (CR=01 e CR=05) ou com movimentações incompletas.

**Ambiente**  
TAF – Nova GIA – A partir da versão 12.1.17.  
  
**Solução**

Possíveis causas do arquivo gerar em branco:

* Configuração incorreta do **Complemento Cadastral;**
* Compartilhamento incorreto de tabelas no **TAF;**
* Erros no **Gerenciador de Integração;**
* *Wizard* Configuração do **TAF** não está apontando para o **banco de dados** correto.

Possíveis causas da geração de valor incorreto (ou a falta de algum **CFOP**):

* Erros no **Gerenciador de Integração;**
* Notas com informações incompletas.

Abaixo existem **Etapas** para o auxilio da identificação e correção dos problemas apontados acima.  
- Se o arquivo foi gerado em branco, siga pela **Etapa 1.**  
- Se apresenta valores incorretos no arquivo, siga pela **Etapa 2.**

OBS: verifique antes das etapas abaixo se o parâmetro **MV\_TAFLPRC** está preenchido com o conteúdo **2000**. O parâmetro em branco pode causar problemas na integração e consequentemente o arquivo ficará incorreto. Após o preenchimento, executar o Processamento novamente.**Etapa 1 : Arquivo em branco.**

Ao gerar o arquivo da **GIA**, é gerado somente com o **CR=01** e **CR=05**.  
Verifique o **Gerenciador de Integração**: [Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - GIA-SP - 6º Passo - Gerenciador de Integração](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035198093-MP-FIS-GIA-SP-6%C2%BA-Passo-Gerenciador-de-Integra%C3%A7%C3%A3o?source=search)Identifique os erros, corrija-os e efetue uma nova geração do arquivo.  
  
Ao acessar o **Gerenciador de Integração**, mesmo tendo executado a rotina **Processamento**e não exibir nenhum *ticket*, o problema pode estar no **Complemento Cadastral** ou na *Wizard* **Configuração do TAF**.

No **Complemento Cadastral**, existem os campos **Filial TAF** que é como a filial está cadastrada no ambiente e campo **Cod. Filial** precisa respeitar o *layout* do seu **SIGAMAT**.Por exemplo: Se o ambiente possuir o **Grupo de Empresa** 01 e a **filial** 01, o **Cód. Filial** no **TAF** será a junção do **Grupo + Filial**, ou seja 0101, então, se o **Cod. Filial** for cadastrado de outra maneira, nenhum dado será exibido pois a integração já envia essas informações com a informação da **filial** para o **TAF**.

Se na *Wizard* de **Configuração do TAF** não for informado corretamente a conexão do **Banco de Dados** do **Protheus**, a integração não ocorrerá, com isso o **Gerenciador de Integração** e consequentemente o arquivo da **GIA** será gerado em branco.  
  
Importante: Se não ocorrer nenhum erro na integração das notas (**Legenda Verde**) e mesmo assim o arquivo continuar em branco, avalie o **compartilhamento das tabelas** **C20**, **C30** e **C2F**.  Caso alguma dessas tabelas esteja compartilhada a rotina não considera as notas que estão no **TAF**.

**Etapa 2: Valores incorretos.**

Verifique o **Gerenciador de Integração**: [Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - GIA-SP - 6º Passo - Gerenciador de Integração](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035198093-MP-FIS-GIA-SP-6%C2%BA-Passo-Gerenciador-de-Integra%C3%A7%C3%A3o?source=search)

Caso identifique erros no **Gerenciador de Integração**, corrija os erros e efetue uma nova geração do arquivo. Caso a integração não ocorra nenhum erro, avalie se as notas integradas estão com os cadastros corretos, as Notas em que o **Cliente** ou **Fornecedor** estão com a **UF** ou **Município** em branco, por exemplo, não são consideradas na geração do arquivo.

Para facilitar a identificação da ocorrência, segue abaixo uma *query*, execute no ambiente do **TAF**.   
Observação: Esse procedimento deve ser realizado por um Analista que possua acesso como administrador e conhecimento em banco de dados.

SELECT C20\_NUMDOC AS Documento, C2F\_VLOPE as ValCont, C20\_UF AS UF\_NOTA, C1H\_UF AS UF\_PART, C1H\_CODMUN AS MUNICIPIO\_PART, C2F\_BASE as BaseICM, C2F\_VALOR as VALICM, C2F\_VLOUTR as OutrosICM, \* FROM C20990 C20  
INNER JOIN C2F990 C2F ON C20.C20\_CHVNF = C2F.C2F\_CHVNF  
INNER JOIN C0Y990 C0Y ON C0Y\_ID = C2F.C2F\_CFOP  
INNER JOIN C1H990 C1H ON C1H\_ID = C20\_CODPAR  
WHERE C20\_DTES BETWEEN  'AAAAMMDDI' AND 'AAAAMMDDF'  
AND C2F\_CODTRI = '000002'  
AND C20\_CODSIT <> '000003'  
AND C20\_FILIAL = 'FILIAL'  
AND C0Y\_CODIGO = 'CFOP'  
AND C20.D\_E\_L\_E\_T\_ = ' '  
AND C2F.D\_E\_L\_E\_T\_ = ' '  
AND C0Y.D\_E\_L\_E\_T\_ = ' '

AND C1H.D\_E\_L\_E\_T\_=' '

Onde:

Nome das tabelas: substituir C20990 pra C20010, ou C20020, por exemplo, conforme seu ambiente;  
'AAAAMMDDI' AND 'AAAAMMDDF': caso o período seja 01/01/2020 a 31/01/2020, alterar para 20200101 e 20200131;  
**CFOP**: Substituir pelo CFOP que apresentou a diferença;  
**FILIAL**: substituir pela filial que está sendo gerada.

Caso identifique o campo **C20\_UF** em branco, edite a nota no **TAF** e preencha esse campo. Caso identifique os campos **C1H\_UF** ou **C1H\_CODMUN** em branco, acesse o cadastro desse Participante no **TAF** e preencha os campos.

Caso os campos do **Cadastro de Clientes/Fornecedores** estejam em branco na origem, preencha também para evitar que o erro ocorra em novas integrações.

Caso as inconsistências persistam após as validações, abra uma solicitação para o Suporte da TOTVS.
