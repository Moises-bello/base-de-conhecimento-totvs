---
article_id: 360051047034
category: Funcionários
content_hash: 2f94712a8a09fb9e231ed75a82eb54b3ad5e82dc013997871a47ffc0e3d549e9
fetched_at: '2026-06-28T22:47:03.408031+00:00'
product: rm
section_id: 1500000861022
source: central-rm
title: RM - FOP - Parametrização (MP 936 - Redução Proporcional de Jornada de Trabalho
  e Salário)
type: support-article
updated_at: '2023-06-28T18:13:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051047034-RM-FOP-Parametriza%C3%A7%C3%A3o-MP-936-Redu%C3%A7%C3%A3o-Proporcional-de-Jornada-de-Trabalho-e-Sal%C3%A1rio
---

**Dúvida**Como parametrizar o sistema para redução proporcional de jornada de trabalho e salário?

**Ambiente**RM - Totvs Folha de Pagamento - Versões:

* **12.1.24.304**
* **12.1.25.291**
* **12.1.26.244**
* **12.1.27.222**
* **12.1.28.135**

**Solução**Como não houve alteração de Jornada no Cadastro do Funcionário, o módulo Folha de Pagamento não irá calcular os dias trabalhados considerando a Redução de Jornada acordada para o cálculo de salário mensal. Neste contexto, orientamos os clientes a criarem uma verba complementar, para descontar o proporcional da redução da Jornada/Salário do funcionário, utilizando fórmula.

Para solucionar essa dúvida, realize os seguintes passos:  
  
**Passo 1**Verifique se os campos do BEM, já aparecem no cadastro do funcionário, em seguida cadastre-os  conforme as informações do acordo. O caminho é: **Administração de pessoal | Funcionários**  | **Selecione o funcionário e clica em editar | No cadastro acesse a opção Registro | B.E.M.**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079677094/mceclip0.png)  
  
Atente-se ao preenchimento dos campos:  
  
**Tipo de adesão:** Redução da Carga Horária  
**Data da Mudança:** Data a ser alimentada no histórico. Não influencia no cálculo da fórmula.  
**Data do acordo:** Dia em que passará a valer o acordo. Influencia no cálculo da fórmula, uma vez que servirá para proporcionalizar o salário a depender dos dias trabalhados com valor reduzido.  
**Percentual de redução da Jornada:** Percentual a ser inserido conforme previsto pela MP, sendo o valor 25, 50 ou 70%.  
**Valor reduzido:** Valor em Reais que será efetivamente reduzido. No exemplo acima, o salário do funcionário é de R$2.000,00. Com a redução de 25%, deve-se preencher, portanto, com R$500,00.  
**Dias de duração do acordo:** Vigência do acordo em dias. A quantidade de dias inserida neste campo encerra o acordo contando a partir da data informada no campo Data do acordo.  
  
**Passo 2**Poderá conferir se gerou o histórico do cadastramento no caminho: **Administração de pessoal | Funcionários | Selecione o funcionário  e clica em Anexos | Históricos | Histórico da Adesão ao Benefício Extraordinário Mensal B.E.M**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080608553/mceclip1.png)  
  
Histórico B.E.M.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080757733/mceclip1.png)  
  
**Passo 3**Cadastre a consulta SQL, disponível no link abaixo:  
- <https://tdn.totvs.com/pages/releaseview.action?pageId=545621517>Obs: no link poderão ser cadastradas a 1º consulta que valida layout do BEM versão 3 ou a 2º consulta ao final da página, que valida o layout 2.

Para cadastrar a consulta SQL, basta acessar: **Gestão | Visões de dados | Seleciona o módulo folha de pagamento e clica em novo**. Criar consulta SQL com **código** BEM:  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080609753/mceclip6.png)  
  
Após cadastrar a consulta e salvar, execute-a selecionando o funcionário em questão, para que veja o resultado que é retornado:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080617093/mceclip0.png)  
  
**Passo 4**Após cadastrar a consulta SQL, poderá cadastrar a fórmula, que ao ser testada para o funcionário, retornará o valor da redução. O caminho para o cadastro da fórmula é: **Administração de pessoal | Fórmulas | Incluir**![mceclip23.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079533394/mceclip23.png)  
  
Faça o cadastro da fórmula, cuja estrutura encontra-se no link disponibilizado no Passo 3, e teste-a inserindo a consulta SQL BEM.  
  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080610393/mceclip8.png)  
  
**Passo 5**

Criar um evento de desconto, sem código de cálculo e informe a fórmula dentro do campo "Fórmula de valor". O caminho para criar o evento é: **Administração de pessoal | Eventos | Incluir**.  
  
![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079530154/mceclip11.png)  
  
**Passo 6**Como se trata de um evento sem código de cálculo, ele não será lançado automaticamente. Dentre as maneiras de se lançar um evento, sugere-se a criação de um grupo de eventos específico. Para a criação do grupo de eventos, o caminho é: **Folha mensal | Lançamentos | Grupo de eventos****![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080611133/mceclip12.png)**Quando acessar os grupos de eventos, clique em **incluir**  
  
![mceclip24.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079533794/mceclip24.png)  
  
Selecione a chapa do funcionário e marque a flag **"Eventos do grupo"** **![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079530294/mceclip13.png)**Dentro da aba **"Eventos do grupo"**, informe o evento de desconto.  
  
**![mceclip16.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080611353/mceclip16.png)**Após informar o evento, retorne a aba **"Identificação"** e lance o grupo de eventos para o envelope do funcionário. A quebra de seção fica a critério da empresa.  
  
![mceclip25.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080616993/mceclip25.png)  
  
Após lançar o grupo de eventos do evento de desconto, poderá lançar o grupo de eventos da folha normal.  
  
![mceclip18.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080616013/mceclip18.png)  
  
Obs: Ao final do processo, no envelope do funcionário, constará as informações da redução de jornada e a folha de pagamento mensal.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079690934/mceclip2.png)
