---
content_hash: cf7d1b38edf2a929d73842d43a893f41e7cd7ac1a25ce877f7fdd21286531be8
fetched_at: '2026-06-29T00:06:25.554453+00:00'
page_id: '224441051'
product: rm
source: tdn-rm
title: DT_CENTRALIZAR_OS_CODIGOS_DE_INTEGRACAO
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_CENTRALIZAR_OS_CODIGOS_DE_INTEGRACAO
version: 139
---

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Framework* |
| **Módulo:** | **EAI** |
|  |  |

## **Descrição**

Essa melhoria no EAI foi criada com o intuito de viabilizar a transferência dos códigos fontes c# (extensions) das integrações atuais (localizados na tabela GsourceCode) para projetos localizados nas *solutions* dos produtos RM.

Com essa mudança esses fontes passarão a ser controlados pelo TFS, possibilitando com isso ganhos de segurança, histórico, controle de concorrência, etc.

## **Escopo da funcionalidade**

****1) - Modelo atual****

Atualmente o analista responsável pelo desenvolvimento da integração pode usar diversos entry Points (gatilhos) disparados durante o processamento da mensagem.

Esses gatilhos possibilitam diversas formas de implementação de customizações.

Códigos C# (.NET) podem ser criados seguindo um modelo padrão e armazenados em uma tabela de banco chamada GSourceCode.

Através das telas do EAI de "cadastro de transformação" e "mapeamento" esses códigos podem ser vinculados a esses gatilhos.

Esse mecanismo de armazenamento de códigos c# na tabela de banco ainda continuará existindo pois integrações totalmente customizadas devem ainda utilizar esse recurso.

Códigos c# existentes na tabela "GSourceCode" e vinculados aos gatilhos terão preferência de execução sobre os fontes localizados em projetos.

**2) - Localização atual dos códigos fontes**

Atualmente, os códigos fontes das integrações estão localizados no projeto "**RM.Con.ConfiguraIntegracao.TotvsMessage**" da solution "Con-EAI" da framework.

Nas pastas "Oracle" e "SQL" (localizadas nesse projeto) foram criados arquivos contendo scripts para vinculação e inclusão desse códigos nas tabelas "GSourceCode", "HCTransformacao" e "HCMapaIntegracao".

Esses scripts são executados automaticamente durante o processo de configuração da integração.

**2) - Transferência dos fontes**

Os scripts abaixo que incluem dados na tabela "GSourceCode"devem ser removidos desses arquivos e transferidos para os projetos nas *solutions* dos produtos.

                   Scripts utilizados:

                    Oracle:

* + 04.1\_SOURCECODE.sql,
  + 04.2\_SOURCECODE\_FinancialNature.sql,
  + 0401\_SOURCECODE\_ORDER.sq

                    Sql:

* + 04.1\_SOURCECODE.sql,
  + 04.2\_SOURCECODE\_FinancialNature.sql,
  + 0401\_SOURCECODE\_ORDER.sql;

Os scripts abaixo que vinculam esses fontes nas tabelas "HCTransformação e HCMapaIntegracao" através dos respectivos campos "IDSRCCUSTOMHANDLE" e "EXTENSION" devem ser alterados.

Nesse caso, deve ser gravada uma string vazia nesses campos.

                  Scripts utilizados:

                    Oracle:

* + 02\_HCTRANSFORMACAO.sql;

                    Sql:

* + 02\_HCTRANSFORMACAO.sql;

Em versões futuras, esses arquivos serão removidos do projeto "**RM.Con.ConfiguraIntegracao.TotvsMessage**".

Atualmente esses códigos fontes estão duplicado em arquivos diferentes (Oracle e sql).

Com essa proposta, existirá uma única classe no projeto, evitando com isso diferenças nesses fontes em bancos diferentes.

Nas integrações em produção, os valores dos campos "**HcTransformacao.IDSRCCUSTOMHANDLE**" e "**HcMapaIntegracao.EXTENSION**" devem ser excluídos (somente para as mensagens que possuem códigos migrados para as dll's).

ex:

* UPDATE hctransformacao  SET IDSRCCUSTOMHANDLE = ' ' where TRANSACTIONID = 'COSTCENTER';
* UPDATE hcmapaintegracao  SET EXTENSION = ' ' where ENTIDADE = 'COSTCENTER';

**3) - Criação dos projetos**

As equipes dos produtos deverão criar projetos nas suas *solutions* contendo classes a serem executadas automaticamente durante o processamento da mensagem.

Passo a passo para criação desses projetos:

a) - No visual Studio, abra a *solution* correspondente a seu segmento. ex. Financeiro.sln.

b) - Crie um novo projeto na solution do tipo "Class Library";

c) - No arquivo AssemblyInfo.cs, utilize o atributo conforme exemplo: [assembly: AssemblyLayerSide(LayerSideKind.Server)];

d) - Adicione referências para as dll's  "RM.Con.TotvsMessage.Extension", "RM.Con.TotvsMessage.IServices", "RM.Con.TotvsMessage.Services";

e) - O projeto recém criado deverá seguir o seguinte padrão de nomenclatura:

**RM.{Segmento}.TotvsMessage.Adapter.dll**,        onde:  Segmento = Sigla do segmento  
                **ex:  RM.Fin.TotvsMessage.Adapter.dll.**

Esse padrão de nomenclatura deve ser seguido corretamente. Caso contrário, a dll não será carregada pela engine do EAI. Consequentemente os fontes da integração não serão executados.

****4) - Criação das classes****

Os códigos localizados na tabela GSourceCode deverão ser transferidos para classes localizadas no projeto recém criado. A criação dessas classes deverá seguir um modelo conforme abaixo:

Códigos que estendem as rotinas de processamento (Extensão de códigos):

       a) - Criar uma classe com um nome qualquer (o ideal seria colocar o nome da mensagem seguido pela versão da mensagem);

**ex: public class CostCenter\_1\_000 : ....**

       b) -  Herdar da classe "**ExtensionBase"** e implementar as interfaces "****IExtensionDataServer, IExtensionTransformReceive, IExtensionWebServices, IExtensionProcess, IExtensionModule, IExtensionMessage"****

**ex: public class **CostCenter\_1\_000**: ExtensionBase, IExtensionDataServer, IExtensionTransformReceive, IExtensionWebServices, IExtensionProcess, IExtensionModule, IExtensionMessage**

        c) - Usar o atributo de classe "**AdapterAttr":**

**ex:**

**[AdapterAttr(TransactionType.ttMensageriaUnica, "COSTCENTER", "2.000")]**  
**public class **CostCenter\_1\_000**: ExtensionBase, IExtensionDataServer, IExtensionTransformReceive, IExtensionWebServices, IExtensionProcess, IExtensionModule, IExtensionMessage**

        d) - Após a criação dessa classe, basta copiar e colar o código fonte (c#) localizado nos scripts, conforme fig abaixo**:**

Códigos que criam manipuladores de recebimento customizados (Handles customizados):

   a) - Criar uma classe com um nome qualquer (o ideal seria colocar o nome da mensagem seguido pela versão da mensagem);

**ex: public class Whois\_******1\_000******: ....**

       b) -  Herdar da classe "**ReceiveMessageHandle****"**

**ex: public class **Whois\_******1\_000********: **ReceiveMessageHandle****

        c) - Usar o atributo de classe "**AdapterAttr":**

**ex:**

**[AdapterAttr(TransactionType.ttMensageriaUnica, "Whois", "1.000")]**  
**public class **Whois\_******1\_000********: ****ReceiveMessageHandle******

        d) - Após a criação dessa classe, basta copiar e colar o código fonte (c#) localizado nos scripts, conforme fig abaixo**:**

divs
