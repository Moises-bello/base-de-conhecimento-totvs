---
article_id: 4414138605463
category: Administração de Pessoal
content_hash: 7aeb09f13b9c7bbf20710992ca637afaacb04619804300b15978e7263c27c059
fetched_at: '2026-06-28T22:47:02.063947+00:00'
product: rm
section_id: 1500000861042
source: central-rm
title: RH - RM - FOP - Parametrização do cálculo de pensão alimentícia na folha
type: support-article
updated_at: '2024-06-17T14:56:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414138605463-RH-RM-FOP-Parametriza%C3%A7%C3%A3o-do-c%C3%A1lculo-de-pens%C3%A3o-aliment%C3%ADcia-na-folha
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20268158643735) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Como realizar a parametrização para o cálculo de pensão alimentícia na folha?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para realizar a parametrização e o cálculo de pensão alimentícia, execute os passos abaixo:  
  
1. Acesse: **Administração de Pessoal | Eventos** e verifique se existe cadastrado o evento de pensão alimentícia como descrito abaixo:  
  
[Código de cálculo 13 - Pensão Alimentícia](https://tdn.totvs.com/pages/viewpage.action?pageId=452718801) - Desconto do tipo valor.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414136639383)  
  
2. Os eventos que deverão ser considerados para o cálculo de pensão alimentícia deverão ter na aba **Inc. Proventos** a Incidências de pensão com a marcação da flag no item Folha, conforme abaixo.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414128615319)  
  
3. Acesse: **Administração de Pessoal | Cadastros Globais | Tabelas Dinâmicas**, selecione a tabela dinâmica **int42** e cadastre as opções de Tipos de Códigos Fixos que poderão ser utilizados para desconto da Pensão.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414128625175)  
  
4. Acesse: **Administração de Pessoal | Funcionários,** selecione o cadastro do funcionário que vai efetuar pagamento de pensão, selecione o campo **Dependentes**. Edite o cadastro do dependente e na pasta **Incidências** marque a incidência de **Pensão.**  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414128756503)  
  
5. Acesse no mesmo cadastro do dependente a pasta **Dados da pensão**. Nesta pasta deverá ser informado a forma como o sistema deve calcular a pensão. Informe no campo **Percentual** o percentual da pensão. Caso algum valor deva ser somado ao cálculo da pensão informe a fórmula com este valor no campo **Fórmula adicional de pensão**. Marque o campo **Ordenado Bruto** caso o queira considerar como base de cálculo da pensão o valor bruto do salário do funcionário, caso o parâmetro fique desmarcado o sistema irá considerar o valor líquido do salário do funcionário.  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414136806423)  
  
Caso exista algum evento que não deva ser considerado no cálculo da pensão informe este evento na pasta **Dependentes | Anexos | Eventos** **não considerados para pensão.**  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414136815511)  
  
6. Acesse o cadastro do funcionário que vai efetuar pagamento de pensão e localize a aba Códigos Fixos. Cadastre os eventos com [Código de Cálculo 13](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=452718801) como Código Fixo Tipo Folha ou Folha/Rescisão, caso deseje descontar a pensão também na rescisão.  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414128765079)  
  
7. Acesse: **Folha Mensal | Lançamentos | Grupo de Eventos**, e edite um Grupo de Eventos e na aba **Códigos Fixos** marque o Código Fixo Folha utilizado no passo anterior, para que o evento Código de Cálculo 13 seja lançado no Envelope de Pagamento do funcionário.  
  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414136825239)  
  
Ao realizar o lançamento do Grupo de Eventos marque na pasta Identificação marque a flag **Lança Códigos Fixos**, salve as alterações e faça o lançamento.  
  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414128770967)  
  
**Saiba mais:**  
[Parametrização para cálculo de Pensão Alimentícia no RM Labore](https://tdn.totvs.com/pages/releaseview.action?pageId=272420775)
