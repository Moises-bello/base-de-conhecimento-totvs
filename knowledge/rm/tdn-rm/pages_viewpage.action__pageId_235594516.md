---
content_hash: 08cdc1676fb0a8e3175fe51904cbc54711f6a6b65b6edd8468b8fb6ac67106a3
fetched_at: '2026-06-29T00:08:05.371557+00:00'
page_id: '235594516'
product: rm
source: tdn-rm
title: ER_PCREQ-9644_Centralizar_Codigos_De_Integração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235594516
version: 122
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | FRAMEWORK | **Módulo** | EAI |
| **Projeto1** | R\_FRW\_FRW002 | **IRM1** | PCREQ-9634 |
| **Requisito1** | PCREQ-9644 | **Subtarefa1** | PDR\_FRW\_FRW002-22 |
| **País** | (X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

Esse documento tem como objetivo propor algumas mudanças no EAI com o intuito de viabilizar a transferência dos códigos fontes c# (extensions) das integrações atuais (localizados na tabela GsourceCode) para projetos localizados nas solutions dos produtos RM. Com essa mudança esses fontes passarão a ser controlados pelo TFS, alcançando ganhos de segurança, controle de históricos, controle de concorrência, etc.

Esse modelo permitirá também que o usuário final (cliente da integração) implemente diversas customizações após execução dos métodos de adapters.

## Definição da Regra de Negócio

## 1) - Modelo atual

 

Características:

 

* O EAI comunica diretamente com extensions (códigos fontes c# responsáveis pela manipulação da mensagem);
* Diferentes extensions podem ser ligados a uma única mensagem no processo de configuração de integração. Para isso, basta criar um mapeamento entre a integração x mensagem, conforme figura 1;
* Extensions são desenvolvidos e mantidos pelas equipes dos produtos (segmentos).
* Extensions podem ser modificados nos clientes em ambiente de teste e produção, visto que os mesmos são abertos para alteração.
* É utilizado um editor de código fonte c# para escrita e compilação conforme a figura 2.
* Esses fontes são armazenados no banco de dados na tabela "GSourceCode".

Vantagens:

a) - Flexibilidade no processo de customização;

Desvantagens:

a) - Possibilita a duplicação de fontes para manipulação de uma mesma mensagem;

b) - Modificações realizadas no fonte para uma determinada integração podem não ser replicadas para outras integrações;

c)- No recebimento de uma determinada mensagem, se existir mais de uma integração cadastrada, o EAI seleciona a primeira integração e executa o código fonte correspondente a essa "integração / mensagem".

d) - Ao executar novamente o configurador, os extensions alterados serão substituídos pela versão atual;

e) - Dificuldade na detecção e análise de erros desses códigos visto que o Editor c# do EAI não oferece suporte para debugger.

## 2) - Modelo proposto

**a) Adapter (Segmentos Totvs)**

* Estrutura a ser utilizada para implementação de regras específicas para manipulação de uma mensagem de integração.
* O EAI comunicará diretamente com os adapters (de responsabilidade das equipes de segmentos);
* Uma "mensagem / versão" estará ligada a um único adapter;
* Regras específicas da mensagem em uma determinada integração devem ser tratadas diretamente no adapter.
* Devem ser mantidos pelas equipes dos produtos (segmentos).
* Não poderão ser modificados pelos clientes pois o código será compilado dentro de dlls nativas dos produtos;
* Estarão localizados na mesma estrutura das solutions dos segmentos no TFS;

b) - **Extensions (customizações)**

 

* Estrutura utilizada para implementação de regras customizadas para um cliente em específico;
* O Editor de código do EAI deve ser usado pelos clientes para implementação de customizações nos adapters dos produtos;

* Esses códigos (extensions) devem ser implementados no contexto da integração em questão.   
  Sendo assim, o cadastro de "Mapa de integração - HCMapaIntegracao" será usado para gravação das regras customizadas a serem implementadas no cliente (customização de integração).
* Os entryPoints das customizações serão disparados imediatamente após a execução do método (de mesmo nome e interface) do adapter;
* Esses recurso permitirá que alterações possam ser feitas nos objetos logo após a execução do código do adapter;

## Detalhamento técnico

**1) - Localização atual dos códigos fontes**

Atualmente, os códigos fontes das integrações estão localizados no projeto "**RM.Con.ConfiguraIntegracao.TotvsMessage**" da solution "Con-EAI" da framework.

Nas pastas "Oracle" e "SQL" (localizadas nesse projeto) foram criados arquivos contendo scripts para vinculação e inclusão desse códigos nas tabelas "GSourceCode", "HCTransformacao" e "HCMapaIntegracao".

Esses scripts são executados automaticamente durante o processo de configuração da integração.

**2) - Transferência dos fontes**

                  a) Os scripts abaixo que incluem dados na tabela "GSourceCode"devem ser removidos desses arquivos e transferidos para os projetos nas solutions dos produtos.

                   Scripts utilizados:

                    Oracle:

* + 04.1\_SOURCECODE.sql,
  + 04.2\_SOURCECODE\_FinancialNature.sql,
  + 0401\_SOURCECODE\_ORDER.sq

                    Sql:

* + 04.1\_SOURCECODE.sql,
  + 04.2\_SOURCECODE\_FinancialNature.sql,
  + 0401\_SOURCECODE\_ORDER.sql;

                b) - Os scripts abaixo que vinculam esses fontes nas tabelas "HCTransformação e HCMapaIntegracao" através dos respectivos campos "IDSRCCUSTOMHANDLE" e "EXTENSION" devem ser alterados.

                        Nesse caso, deve ser gravada uma string vazia nesses campos.

                  Scripts utilizados:

                    Oracle:

* + 02\_HCTRANSFORMACAO.sql;

                    Sql:

* + 02\_HCTRANSFORMACAO.sql;

Em versões futuras, esses arquivos serão removidos do projeto "**RM.Con.ConfiguraIntegracao.TotvsMessage**".

Atualmente esses códigos fontes estão duplicado em arquivos diferentes (Oracle e sql).

Com essa proposta, existirá uma única classe no projeto, evitando com isso diferenças nesses fontes em bancos diferentes.

Nas integrações em produção, os valores dos campos "**HcTransformacao.IDSRCCUSTOMHANDLE**" e "**HcMapaIntegracao.EXTENSION**" devem ser excluídos **ou** alterados para manter somente regras customizadas.

ex:

* UPDATE hctransformacao  SET IDSRCCUSTOMHANDLE = ' ' where TRANSACTIONID = 'COSTCENTER';
* UPDATE hcmapaintegracao  SET EXTENSION = ' ' where ENTIDADE = 'COSTCENTER';

**3) - Criação dos projetos**

As equipes dos produtos deverão criar projetos nas suas solutions contendo classes a serem executadas automaticamente durante o processamento da mensagem.

Passo a passo para criação desses projetos:

a) - No visual Studio, abra a solution correspondente ao determinado segmento. ex. Financeiro.sln.

b) - Crie um novo projeto na solution do tipo "Class Library";

c) - No arquivo AssemblyInfo.cs, utilize o atributo conforme exemplo: [assembly: AssemblyLayerSide(LayerSideKind.Server)];

d) - Adicione referências para as dll's  "RM.Con.TotvsMessage.Extension", "RM.Con.TotvsMessage.IServices", "RM.Con.TotvsMessage.Services";

e) - O projeto recém criado deverá seguir o seguinte padrão de nomenclatura:

**RM.{Segmento}.TotvsMessage.Adapter.dll**,        onde:  Segmento = Sigla do segmento  
               **ex:  RM.Fin.TotvsMessage.Adapter.dll.**

Esse padrão de nomenclatura deve ser seguido corretamente. Caso contrário, a dll não será carregada pela engine do EAI. Consequentemente os adapters da integração não serão executados.

**4) - Criação das classes**

Os códigos localizados na tabela GSourceCode deverão ser transferidos para classes localizadas no projeto recém criado. A criação dessas classes deverá seguir um modelo conforme abaixo:

**4.1 - Códigos que estendem as rotinas de processamento (Extensão de códigos):**

       a) - Criar uma classe com um nome qualquer (o ideal seria colocar o nome da mensagem seguido pela versão da mensagem);

**ex: public class CostCenter\_1\_000 : ....**

       b) -  Herdar da classe "**AdapterBase"** sobrescrevendo os métodos necessários;

**ex: public class **CostCenter\_1\_000**: AdapterBase**

        c) - Usar o atributo de classe "**AdapterAttr":**

Esse atributo irá "carimbar" a classe com informações do adapter.

No exemplo abaixo, o adapter somente será carregado no ***recebimento*** de uma mensagem COSTCENTER 2.000.

**ex:**

**[AdapterAttr(TransactionType.ttMensageriaUnica, AdapterType.atReceive, "COSTCENTER", "2.000")]**  
**public class **CostCenter\_2\_000**: AdapterBase**

        d) - Após a criação dessa classe, basta copiar e colar o código fonte (c#) localizado nos scripts, substituindo os nomes dos métodos "incluindo a palavro **Do** antes do nome do método" e usando um "override" no início do mesmo:

Dica de implementação

Seguindo o exemplo acima, o ideal seria criar uma classe chamada "CostCenterBase" herdando da classe "AdapterBase" (nesse caso não será utilizado o atributo "AbapterAttr".

Sendo assim, serão criadas as classes "CostCenter\_1\_000" e "CostCenter\_2\_000 herdando da classe "CostCenterBase" (nesse caso o atributio "AdapterAttr" será utilizado nas classes descendentes).

Através desse mecanismo de orientação a objetos códigos poderão ser reaproveitados nas diversas versões da mesma mensagem.

                  Modelagem de classes.

| Classe | Descrição |
| --- | --- |
| CustomBase | Classe ancestral usada para definir métodos e propriedades genéricos para as classes concretas para manipulação das mensagens |
| AdapterBase | Classe ancestral usada para definir regras comuns para todos os adapters. |
| ExtensionBase | Classe ancestral usada para definir regras comuns para todos os extensions (estruturas a serem usadas para inclusão de códigos customizados pelos clientes) |

**4.2 - Códigos que criam manipuladores de recebimento customizados (Handles customizados):**

* Adapters de recebimento são estruturas utilizadas para implementar toda a regra de negócio de manipulação da mensagem de recebimento.
* Eles são ligados diretamente na mensagem e não na mensagem / integração (como ocorre com os extensions) conforme figura 3.
* São estruturas menos utilizadas, visto que a maioria das mensagens de recebimento são manipuladas por dataServers;
* Eles devem ser migrados para estruturas de adapters da mesma forma que o extensions;

   a) - Criar uma classe com um nome qualquer (o ideal seria colocar o nome da mensagem seguido pela versão da mensagem);

**ex: public class Whois\_******1\_000******: ....**

       b) -  Herdar da classe "**AdapterReceiveBase****"**

**ex: public class **Whois\_******1\_000********: **AdapterMessageBase****

        c) - Usar o atributo de classe "**AdapterAttr":**

**ex:**

**[AdapterAttr(TransactionType.ttMensageriaUnica, "Whois", "1.000")]**  
**public class **Whois\_******1\_000********: ****AdapterReceiveBase******

        d) - Após a criação dessa classe, basta copiar e colar o código fonte (c#) localizado nos scripts, conforme fig abaixo**:**

 Modelagem de classes.

| Classe | Descrição |
| --- | --- |
| ReceiveMessageHandle | Manipulador original do EAI para mensagens de recebimento |
| AdapterReceiveBase | Classe ancestral usada para definir regras comuns para todos os adapters de customHandle de recebimento |

## Protótipos de Tela

Figura1 - Mapeamento mensagem x integração

figura2: Editor de  código fonte do EAI

figura 3: Adapter de recebimento

## 

### 

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
