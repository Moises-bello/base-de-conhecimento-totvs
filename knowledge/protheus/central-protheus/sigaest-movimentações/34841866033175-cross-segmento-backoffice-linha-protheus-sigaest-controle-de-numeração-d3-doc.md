---
article_id: 34841866033175
category: SIGAEST - MOVIMENTAÇÕES
content_hash: a374c09802d915e6ae2b79b11ef26539bba197afe934dadb4fcbe6e7becc4f4f
fetched_at: '2026-06-28T22:38:54.219823+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST -  Controle de numeração
  D3_DOC
type: support-article
updated_at: '2026-06-19T15:40:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34841866033175-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Controle-de-numera%C3%A7%C3%A3o-D3-DOC
---

O campo D3\_DOC na tabela SD3 do Protheus armazena números de documentos em movimentos de estoque, controlados pela variável cDocumento nas rotinas MATA241 e MATA242 de acordo digitação do usuário. A numeração é sequencial automática, mas pode ser alterada manualmente, o que pode causar inconsistências, especialmente com caracteres especiais ou espaços. Recomenda-se evitar digitação manual, revisar a base e garantir collation correto no banco. Correções podem ser feitas via estorno, ajuste por DBA, customização ou bloqueio da digitação manual.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34841866013463) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como funciona o controle de numeração do campo D3\_DOC no Protheus?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
O campo **D3\_DOC**, da tabela **SD3**, é responsável por armazenar o número do documento associado a determinados movimentos de estoque.  
O controle e a numeração deste campo são realizados por meio de funções internas, que pegam o proximo numero maior disponivel na base de dados em relação a tabela SD3, utilizada nas rotinas de movimentações, onde vamos abordar aqui no caso as rotinas MATA241,MATA242 E MATA261.

**Este KCS tem como objetivo esclarecer:**

* Como o campo D3\_DOC é gravado;
* Quais cuidados devem ser observados;
* Como proceder em caso de inconsistências;
* Quais alternativas existem para correção e controle.

### **Onde o campo é usado nas rotinas em questão**

* Movimentação Múltipla (MATA241)
* Desmontagem de Produto (MATA242)
* Transferência Múltipla (MATA261)

utilizam a variável **cDocumento** para definir o valor do campo **D3\_DOC** durante a digitação.

Por padrão, **não há restrição quanto ao que pode ser digitado nesse campo**. Entretanto, é necessário **cautela no uso de caracteres especiais**, tais como:

```
!   @   #   $   %   ^   &   *   (   )   _   -   +   =   {   }  
[   ]   |   \   :   ;   "   '   <   >   ,   .   ?   /   ~   `  "espaço"
```

**O uso desses caracteres pode:**

* Impactar processos internos do sistema;
* Causar a busca incorreta do próximo número sequencial (tratamento alfanumérico);
* Gerar inconsistências dependendo do **SGBD** utilizado (ex.: Oracle, PostgreSQL, etc.).

### **Como o sistema gera a numeração**

Para garantir um controle saudável da numeração, o sistema possui uma **regra interna padrão**, que sugere o preenchimento sequencial do campo **D3\_DOC**:

```
cDocumento := IIf(Empty(cDocumento), NextNumero("SD3", 2, "D3_DOC", .T.), cDocumento)
```

Ou seja:

* Se a variável **cDocumento** estiver vazia, o sistema busca automaticamente o próximo número disponível;
* Caso o usuário digite manualmente um valor, esse será considerado como base para a sequência.

### **Exemplo prático**

Imagine que sua numeração atual esteja em **000099**.  
Se, por engano, alguém digitar manualmente o valor **100050**, o próximo documento gravado será **100051**, pois o sistema sempre identifica o **maior número sequencial disponível**.  
Com isso, a sequência esperada (**000100**) será quebrada.

### **Possíveis inconsistências**

O campo **D3\_DOC** pode apresentar problemas quando contém:

* **Caracteres especiais**;
* **Espaços em branco**;
* **Sequências manuais fora do padrão**.

Essas situações não configuram erro do sistema, mas sim **efeitos colaterais de digitação indevida**.

Além disso, é essencial verificar se o **Collation** do banco de dados está configurado corretamente.  
[Clique aqui e acesse a FAQ com orientações sobre Collation por SGBD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000513567-Framework-Linha-Protheus-Qual-Collation-utilizar-na-cria%C3%A7%C3%A3o-do-Banco-de-Dados).

### **Como corrigir a sequência?**

Se ocorrer erro de digitação ou quebra da sequência, existem quatro alternativas:

### 

### **1. Estorno do movimento e exclusão física do mesmo**

Caso tenha sido movimentos recentes e houver a possibilidade de estorno, e processar a rotina [Recalculo do Custo Médio (MATA330)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024805291) com o pergunte "[Apaga Estornos = SIM](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024805291-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Perguntas-do-Rec%C3%A1lculo-do-Custo-M%C3%A9dio#:~:text=n%C3%A3o%20receber%C3%A3o%20lan%C3%A7amentos).-,Apaga%20Estornos,-%3A)" para que os estornos sejam excluídos fisicamente do banco. Forma mais rápida e ágil para solução.

### **2. Ajuste com DBA ou ANALISTA IN LOCO**

Nos casos em que o campo D3\_DOC apresente conteúdos incorretos e o sistema impeça o estorno pelos meios convencionais, que não possa ser realizado pelo cliente, impossibilitando o retorno ao sequencial anterior.

Recomendamos não realizar ajustes manuais via banco de dados sem supervisão técnica. Para restabelecer a integridade do sequencial e das tabelas de movimentação, **a orientação é o acionamento de um consultor especialista in loco, com domínio em Estoque e Custos e banco de dados**, para a realização de ajustes pontuais e seguros na base de dados.

### **3. Customização do campo**

Implementar uma regra personalizada para que a numeração seja gravada de acordo com a necessidade do cliente, após ajustes necessarios dos dados incorretos. Veja mais informações na Documentação: [**Ajuste da Numeração do Campo D3\_DOC por customização do campo**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/38618849705879-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Ajuste-da-Numera%C3%A7%C3%A3o-do-Campo-D3-DOC-por-Customiza%C3%A7%C3%A3o-do-campo)

### **4. Bloqueio da digitação manual**

Configurar o sistema para que o campo **cDocumento (D3\_DOC)** não possa ser digitado manualmente, mantendo assim apenas o **controle automático sequencial**.

### **Possuo de forma legado, campos com caracter minusculo e maiusculo, e preciso considerar os minusculos, o que fazer?**

Criado o parametro [**MV\_ESTMINU**](https://tdn.totvs.com/x/oxW5Pg) que ativo vai permitir o uso de minusculas no documento, pois nas versões mais recentes, o controle de numeração segue apenas para caracteres maiusculos sequenciais.

**No Configurador (SIGACFG), acesse Ambientes / Cadastros / Parâmetros (CFGX017). Crie o parâmetro a seguir:**

| **Nome** | MV\_ESTMINU |
| --- | --- |
| Tipo | L |
| **Cont. Por** | .T. |
| Descrição | Define se permite o uso de minusculas no numero do documento  .T. = Sim; .F. = Não (default) |
|

### **Recomendações finais**

* Sempre que possível, evite a digitação manual no campo **D3\_DOC**;
* Prefira o uso do controle automático oferecido pela regra interna do sistema;
* Revise periodicamente a base de dados para identificar inconsistências;
* Garanta que o **Collation** esteja correto para evitar problemas de ordenação.
* Para assuntos sobre customizações TOTVS, o time de Suporte consistirá em fornecer as documentações que possibilitem a utilização de pontos de entrada e rotinas automáticas documentadas  no portal TDN para uso no produto padrão.  
  Estas documentações possuem exemplos de utilização previamente testados, caso utilize estes e o resultado seja diferente do documentado ou apresente falha, caso não disponha de analista programador para realizar os ajustes, dispomos do serviço do time Hub Plataformas ([hub.plataformas@totvs.com.br](mailto:hub.plataformas@totvs.com.br)).   
  Esta equipe oferece os serviços de criação e manutenção de fontes Protheus, que tem como característica a disponibilidade de um recurso remoto para realização desta atividade em horários comerciais (dias úteis das 08:00 às 18:00).

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
