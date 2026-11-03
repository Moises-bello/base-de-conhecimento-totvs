---
article_id: 4424755735575
category: FÉRIAS
content_hash: d69f2f1c0321d2c0d7c20705a1d74a4b20cafee2caa4ab4ebe6a0a7d85f52566
fetched_at: '2026-06-28T22:44:34.562358+00:00'
product: protheus
section_id: 10299705719575
source: central-protheus
title: RH - Linha Protheus - MEU RH - É possível o Gestor saber a quantidade de funcionários
  que possuem férias vencidas, férias em dobro, ou a vencer
type: support-article
updated_at: '2026-06-26T20:58:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4424755735575-RH-Linha-Protheus-MEU-RH-%C3%89-poss%C3%ADvel-o-Gestor-saber-a-quantidade-de-funcion%C3%A1rios-que-possuem-f%C3%A9rias-vencidas-f%C3%A9rias-em-dobro-ou-a-vencer
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22596011420951) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
É possível o Gestor saber a quantidade de funcionários que possuem férias vencidas, férias em dobro, ou a vencer  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - MEU RH - todas as versões  
  
**Solução**  
Foi implementado um novo recurso na tela de Gestão de Férias, que agora passa a apresentar no topo da página um totalizador obtido a partir de uma soma que considera a situação de férias dos funcionários da equipe.  
  
Conforme a imagem abaixo, o contador será composto por 5 colunas, com os seguintes itens: Em Férias, Vencidas, A vencer, Em dobro e Risco de dobro.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4424790942487)  
  
**Critérios para contagem**  
O contador será composto à partir da avaliação de cada funcionário que compõe a equipe do gestor, e para soma serão avaliados os dados do Controle Dias de Direito (tabela SRF) e do Cabeçalho de Férias (tabela SRH).   
  
Os critérios considerados para a soma de cada coluna estão descritos abaixo:

* **Em férias**  
  Funcionários que possuem cálculo de férias e a data de início das férias é menor ou igual ao dia atual, e a data de término das férias é menor ou igual ao dia atual.
* **Vencidas**  
  Funcionários que possuem cadastro na programação de férias (SRF), em que o campo "*Dias de Férias Vencidas*" (RF\_DFERVAT) é maior que 0
* **A vencer**  
  Funcionários que possuem cadastro na programação de férias (SRF), em que o campo "*Dias de Férias Proporcionais*" (RF\_DFERAAT) é maior que 0
* **Em dobro**  
  Funcionários que possuem cadastro na programação de férias (SRF), em que o período concessivo já está vencido.
* **Risco de dobro**  
  Funcionários que possuem cadastro na programação de férias (SRF), em que o período concessivo vencerá em 60 dias ou menos.  
  Observação: os 60 são contados considerando o término do período concessivo com a subtração dos dias de férias que o funcionário tem direito.

Para férias em **Risco de Dobro,** não será apresentado o botão **SOLICITAR** para o gestor.   
Para que ele possa administrar e solicitar férias para estes trabalhadores, é preciso utilizar o botão de **encaminhamento**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22596065998743)

**Considerações sobre o contador**

* Para que o contador apresente os valores corretos é imprescindível que os dados da programação de férias (tabela SRF) esteja saneada e correta, sem dados inválidos ou inconsistentes.
* A contagem será feita considerando apenas um registro por funcionário a partir de seu registro ativo mais antigo na programação de férias (tabela SRF). Exemplo: o funcionário tem 2 registros ativos, um deles está com o período concessivo vencido (férias em dobro) e outro com dias vencidos (férias vencidas), nesse caso o contador irá apresentar o valor 1 na coluna férias em dobro.
* A contagem será aplicada apenas aos funcionários que se enquadram estritamente nos itens descritos em "**Critérios para contagem**". Ou seja, há situações em que um determinado funcionário não será considerado no contador por não se enquadrar em nenhum dos critérios pré-estabelecidos. São as seguintes situações:  
    
  1. Férias calculadas em data futura: pode ser cálculo total ou parcial dos dias de direito, e é indiferente o estado que se encontra o período aquisitivo (com dias vencidos, vencidos em dobro ou a vencer).   
    
  2. Férias já programadas: pode ser programação total ou parcial do período, e os dias programados podem ter sido originados em uma solicitação do funcionário, ou cadastrados diretamente pelo RH.

* Cada opção de filtro do contador é individual, ou seja, somente 1 filtro deverá ser efetuado por seleção.

![Contador_Gest_o_de_F_rias_MEURH.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4424755112215)  
  
**Documento de referência:** [**Monitor de Férias - Contador**](https://tdn.totvs.com/pages/viewpage.action?pageId=658408844)  
  
**Saiba mais:**  
[**RH - Linha Protheus - MEU RH - O gestor pode solicitar as férias do funcionário pelo MEU RH**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402719334551)  
[**RH - Linha Protheus - MEU RH - É possível o gestor informar o motivo da rejeição na solicitação de férias**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4421278138391)  
[**RH - Linha Protheus - MEU RH - É possível o Gestor ter maiores informações das férias dos funcionários na rotina Gestão de Férias**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4424781949079)  
[**CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI para acessar a documentação de referência sobre o MEU RH**](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
