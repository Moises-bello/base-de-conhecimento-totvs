---
article_id: 39873578343447
category: Gestão
content_hash: 8cf49d3bdfefea2406c005f38285fa8dea50d02702df6c9922c0d8a5b18628ea
fetched_at: '2026-06-28T22:46:48.217888+00:00'
product: rm
section_id: 1500000861162
source: central-rm
title: RH - RM - FOP - Como importar e gerar relatórios Smart View
type: support-article
updated_at: '2026-06-11T19:41:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39873578343447-RH-RM-FOP-Como-importar-e-gerar-relat%C3%B3rios-Smart-View
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39873578332695) Tempo aproximado para leitura: **00:03:45 min**  
  
**Dúvida**  
Como importar e gerar relatórios Smart View?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - 12.1.2502, 12.1.2506, 12.1.2510, 12.1.2602 ou superiores.  
  
**Solução**

Para solucionar essa dúvida, realize os seguintes passos:

**Importação dos relatórios.**

**Para realizar a importação dos relatórios deve seguir o seguinte caminho:**

1. Acesse: **Gestão | Totvs Compartilhamento.**  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39874118041239)  
  
2. Para localizar os arquivos, utilize os filtros: **Buscar**, **Tipo** e **Produto**. No exemplo abaixo, mostraremos como buscar relatórios da Folha de Pagamento.  
  
Campo **Buscar**: deixa em branco;  
Campo **Tipo**: informe Recursos Smart View;  
Campo **Produto**: Folha de Pagamento;  
  
3. Após parametrizar os campos, conforme orientado no passo anterior, clique na opção**Pesquisar**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39874080640023)  
  
Todos os relatórios **Smart View para o sistema de Folha de Pagamento** serão exibidos.  
  
4. Selecione o relatório desejado e clique no botão **Download**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39874378294679)

6. Assim, as opções Salvar e Importar serão exibidas. Se quiser armazenar o relatório, clique nesta opção. Se não for o caso, se desejar realizar a importação, clique na opção Importar.  
  
**Geração do relatório.**

Depois de concluir todas as etapas de importação, veja as instruções para gerar os relatórios.  
  
1. Depois de importar, o relatório será salvo em Gestão | Smart View. busque e selecione o relatório. No exemplo vou utilizar o relatório de Ficha financeira FOPTRP0008 Ficha financeira.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39874847331735)

2. Após selecionar o relatório clique na opção**"Mais Ações" Executar em SmartView**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39874843689879)

3.  Será necessário agora preencher os parâmetros obrigatórios, que são:

* **Código da Coligada (Poderá ser utilizado N Coligadas, basta clicar no ícone de adição ![](https://tdn.totvs.com/download/thumbnails/804054467/image-2024-1-4_16-53-56.png?version=1&modificationDate=1704398036633&api=v2) ou ( -1 ) para trazer todas coligadas.**
* **Chapa do Funcionário**(Poderá ser utilizado N Chapa de Funcionários, basta clicar no ícone de adição ![](https://tdn.totvs.com/download/thumbnails/804054467/image-2024-1-4_16-53-56.png?version=1&modificationDate=1704398036633&api=v2) ou -1 para trazer todos funcionários.
* **Ano Inicial**
* **Ano Final**
* **Mês Inicial**
* **Mês Final**
* **Período**(Poderá ser utilizado N períodos, basta clicar no ícone de adição ![](https://tdn.totvs.com/download/thumbnails/804054467/image-2024-1-4_16-53-56.png?version=1&modificationDate=1704398036633&api=v2) ou ( -1 )para trazer todos períodos.
* **Cod. Seção**(Pode ser utilizado como "Similaridade" Exemplo: Cód. Seção 02 Deverá ser retornado funcionários da Seção 01.02 / 02 / 02.01 / 03.02 / 04.02 ) ou ( -1 )para trazer todas seções.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39874847335831)

Depois de preencher todas as informações dos filtros, clique na opção Enviar. O relatório será exibido no lado esquerdo do filtro.

**Observação**  
Os parametros que estão em negrito são obrigatórios, como por exemplo;

* **Código da Coligada**
* **Chapa do Funcionário**
* **Ano Inicial**
* **Ano Final**
* **Mês Inicial**
* **Mês Final**

Se as informações nos campos obrigatórios não forem preenchidas, ao clicar na opção de enviar, o sistema exibirá uma mensagem de erro: **"O conteúdo retornado pelo ERP TOTVS não condiz com o padrão"**. No meu exemplo, deixei o campo Chapa do funcionário vazio.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39875522665239)

Para a correção basta clicar no ícone de adição ![](https://tdn.totvs.com/download/thumbnails/804054467/image-2024-1-4_16-53-56.png?version=1&modificationDate=1704398036633&api=v2) e informar ( -1 ) para trazer todos funcionários ou informar a chapa do funcionário, conforme exemplo da imagem anterior.

**Informações complementares**

O **Smart View**é uma aplicação web, independente de linha e multiplataforma (Windows e Linux) que possui ferramentas para design e geração de relatórios e visualização e análise de dados transacionais.

Em resumo, o **Smart View**é a solução TOTVS para auxiliar a análise dos dados dos softwares de gestão e para impulsionar negócios oferecendo acesso rápido e descomplicado às informações.

**Importante**

No caso dos relatórios do RM Reports que já estão disponíveis no Smart View, a TOTVS está iniciando a comunicação sobre o ciclo de vida desses relatórios com o objetivo de orientar os clientes quanto à migração para o Smart View, assegurando a continuidade e a modernização das soluções utilizadas.

Além disso, informamos que **não haverá mais manutenção para esses relatórios na ferramenta RM Reports**. Todos os **novos relatórios disponibilizados pela TOTVS Folha de Pagamento passarão a ser desenvolvidos exclusivamente no Smart View**.

Mas por que, às vezes, é necessário descontinuar?

Porque é justamente essa transição que viabiliza a adoção de novas tecnologias mais modernas, com melhor desempenho, layout mais intuitivo e atual, além de melhorias significativas na usabilidade.

No caso do Smart View, por exemplo, os relatórios contam com configurações personalizadas por usuário, objetos de negócio mais flexíveis e uma estrutura otimizada para performance de dados. Tudo isso proporciona uma experiência mais ágil, eficiente e alinhada às necessidades do dia a dia.

Esse processo se estende de 6 meses a um ano.  
  
**O RM Reports como ferramenta não tem prevista a sua descontinuação.**

O que está em andamento é o processo de **descontinuidade dos relatórios do Book de RH desenvolvidos no RM Reports**, que já foram migrados para a ferramenta Smart View.

Essa transição tem como objetivo incentivar o uso da nova tecnologia, que oferece mais desempenho, usabilidade e alinhamento com a evolução da plataforma TOTVS Folha de Pagamento.  
  
**Saiba mais**  
[Passo a Passo da Convergência no Smart View](https://tdn.totvs.com/pages/releaseview.action?pageId=954104268)   
[RH - RM - FOP- Importação de relatórios e layouts através do Totvs Compartilhamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7781155867543-RH-RM-FOP-Importa%C3%A7%C3%A3o-de-relat%C3%B3rios-e-layouts-atrav%C3%A9s-do-Totvs-Compartilhamento)  
[Introdução Smart View](https://O%20Smart%20View%20%C3%A9%20uma%20aplica%C3%A7%C3%A3o%20web,%20independente%20de%20linha%20e%20multiplataforma%20(Windows%20e%20Linux)%20que%20possui%20ferramentas%20para%20design%20e%20gera%C3%A7%C3%A3o%20de%20relat%C3%B3rios%20e%20visualiza%C3%A7%C3%A3o%20e%20an%C3%A1lise%20de%20dados%20transacionais.%20Em%20resumo,%20o%20Smart%20View%20%C3%A9%20a%20solu%C3%A7%C3%A3o%20TOTVS%20para%20auxiliar%20a%20an%C3%A1lise%20dos%20dados%20dos%20softwares%20de%20gest%C3%A3o%20e%20para%20impulsionar%20neg%C3%B3cios%20oferecendo%20acesso%20r%C3%A1pido%20e%20descomplicado%20%C3%A0s%20informa%C3%A7%C3%B5es.)
