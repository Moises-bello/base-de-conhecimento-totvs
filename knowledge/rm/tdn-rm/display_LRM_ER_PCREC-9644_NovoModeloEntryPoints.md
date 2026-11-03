---
content_hash: 66c19eb66970fc9fa4e00386d529ca8eeb72780dce849206c582e55ae42e8d1f
fetched_at: '2026-06-29T00:06:28.575999+00:00'
page_id: '233755390'
product: rm
source: tdn-rm
title: ER_PCREC-9644_NovoModeloEntryPoints
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREC-9644_NovoModeloEntryPoints
version: 142
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo: Integração (EAI)** |  |
| **Segmento Executor** | Framework | | |
| **Projeto1** | R\_FRW004 | **IRM1 : PCREC-9634** |  |
| **Requisito1** | PCREC-9644 | **Subtarefa1: PDR\_FRW\_FRW002-22** |  |
| **Chamado2** |  | | |
| **País** | (  ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

## Objetivo

**Permitir que o usuário final (cliente da integração) customize um adapter e não a mensagem.**

## Definição da Regra de Negócio

 

## 1) - Modelo atual

Características:

* O EAI comunica diretamente com extensions (códigos fontes c# responsáveis pela manipulação da mensagem);
* Diferentes extensions podem ser ligados a uma única mensagem no processo de configuração de integração. Para isso, basta criar um mapeamento entre a integração x mensagem conforme figura 1.
* Extensions são desenvolvidos e mantidos pelas equipes dos produtos (segmentos).
* Extensions podem ser modificados nos clientes em ambiente de teste e produção, visto que os mesmos são abertos para alteração.
* É utilizado um editor de código fonte c# para escrita e compilação conforme a figura 2.
* Esses fontes são armazenados no banco de dados na tabela "GSourceCode".

Vantagens:

a) - Flexibilidade no processo de customização;

Desvantagens:

a) - Possibilita a duplicação de fontes para manipulação de uma mesma mensagem;

b) - Modificações realizadas no fonte para uma determinada integração podem não ser replicadas para outras integrações;

c)- No recebimento de uma determinada mensagem, se existir mais de uma integração cadastrada, o EAI seleciona a primeira integração e executa o código fonte correspondente a essa integração / mensagem.

d) - Ao executar novamente o configurador em ambiente do cliente, os extensions alterados serão substituídos pela versão atual;

e) - Dificuldade na detecção e análise de erros desses códigos visto que o Editor c# do EAI não oferece suporte para debugger.

## 2) - Modelo proposto

**Adapters**:

* Estrutura a ser utilizada para implementação de regras específicas para manipulação de uma mensagem de integração.
* O EAI comunicará diretamente com os adapters (de responsabilidade das equipes de segmentos);
* Uma mensagem / versão estará ligada a um único adapter;
* Regras específicas da mensagem em uma determinada integração devem ser tratadas diretamente no adapter.
* Devem ser mantidos pelas equipes dos produtos (segmentos).
* Não poderão ser modificados pelos clientes pois o código será compilado dentro das dlls nativas do produto;
* Estarão localizados na mesma estrutura das solutions dos segmentos no TFS;

b) - **Extensions**

* Estrutura utilizada para implementação de regras customizadas para um cliente em específico;
* O Editor de código do EAI deve ser usado pelos clientes para implementação de customizações nos adapters dos produtos;

* Esses códigos (extensions) devem ser implementados no contexto da integração em questão.   
  Sendo assim, o cadastro de "Mapa de integração" será usado para gravação das regras customizadas a serem implementadas no cliente (customização de integração).
* Os entryPoints das customizações serão disparados imediatamente após a execução do método (de mesmo nome e interface) do adapter;
* Esses recurso permitirá que alterações possam ser feitas nos objetos logo após a execução do código do adapter;

## 2.1) - Exemplos de implementação do novo modelo.

ex:  Manipulação da mensagem COSTCENTER.

a) Criação do adapter.

* As regras de negócio escritas atualmente no extension para manipulação da mensagem COSTCENTER devem ser transferidas para classes que herdam de AdapterBase, conforme print abaixo.
* Conforme exemplo abaixo, o método DoAfterTransformDataSet será chamado no momento da transformação da mensagem única para o formato nativo do centro de custo.

a) Criação do extension.

* O recurso de extension pode ser usado para inclusão de códigos customizados no ambiente do cliente;
* Após execução do método DoAfterTransformDataSet" localizado no adapter acima, o método "AfterTransformDataSet" localizado abaixo no extension será chamado.
* Esse mecanismo possibilitará a implementação de códigos customizados a serem disparados imediatamente após a execução do adapter.

## 2.3) - Modelagem de classes.

a) - CustomBase - classe ancestral usada para definir métodos e propriedades genérico para as classes concretas para manipulação das mensagens;

b) - AdapterBase - classe ancestral usada para definir regras comuns para todos os adapters;

c) - ExtensionBase - classe ancestral usada para definir regras comuns para todos os extensions (estruturas a serem usadas para inclusão de códigos customizados pelos clientes).

## 3) - Modelo proposto para os adapters de recebimento (CustomHandle).

* Adapters de recebimento são estruturas utilizadas para implementar toda a regra de negócio de manipulação da mensagem de recebimento.
* Eles são ligados diretamente na mensagem e não na mensagem / integração (como ocorre com os extensions) conforme figura 3.
* São estruturas menos utilizadas, visto que a maioria das mensagens de recebimento são manipuladas por dataServers;
* Eles devem ser migrados para estruturas de adapters da mesma forma que o extensions;
* Caso exista um extension cadastrado no cliente para esse adapter de recebimento, o mesmo será usado pela engine do EAI substituindo assim o adapter localizado na dll;

### Opcional

## Protótipo de Tela

Figura1 - Mapeamento mensagem x integração

figura2: Editor de  código fonte do EAI

figura 3: Adapter de recebimento

## 

### 

---

[

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
