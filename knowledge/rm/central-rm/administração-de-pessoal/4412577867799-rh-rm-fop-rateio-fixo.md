---
article_id: 4412577867799
category: Administração de Pessoal
content_hash: 33a88a825099a3f23cf14560207c1269f04a271e80ec4546b0e4fb3dc9a90112
fetched_at: '2026-06-28T22:47:02.111583+00:00'
product: rm
section_id: 1500000861042
source: central-rm
title: RH - RM - FOP - Rateio Fixo
type: support-article
updated_at: '2024-06-14T14:48:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412577867799-RH-RM-FOP-Rateio-Fixo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24182655831063)**Tempo aproximado para leitura: **00:02:30 min  
  
Dúvida**Como cadastro o rateio fixo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões

**Solução**O rateio é realizado através dos centros de custos, que é onde as despesas serão contabilizadas. Para isso, é necessário verificar se o sistema está parametrizado para utilizar centro de custo:  
Acesse: Configurações | Parametrizador| Folha normal | Cálculo 2/2:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412661750423)  
  
Dessa forma, cada centro de custo onde o funcionário trabalhou durante o mês será utilizado para que o sistema faça o rateio durante o cálculo por centro de custo. Deve-se informar o percentual de rateio fixo no qual o funcionário trabalhou em determinado centro de custo. A soma dos percentuais deverá ser igual a 100%, já que, para o cálculo o sistema dividirá por 100. Para fazer o cadastro, acesse o funcionário | Anexo | Folha de Pagamento | Rateio Fixo:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412652507799)  
  
Caso o parâmetro **Rateio fixo por valor** estiver marcado, o campo acima será renomeado para **Valor** e deverão ser informados valores brutos para se chegar aos percentuais usados no rateio.  
  
Por exemplo, o rateio fixo do funcionário está preenchido com os seguintes dados:  
Centro de Custo Valor  
XXXX   54,00  
YYYY   66,00  
Total do Rateio  120,00  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412661776791)  
  
Ao ratear um evento com o valor de R$29,68, o sistema fará o seguinte cálculo:  
Centro de custo XXXX = R$29,68 \* 54 / 120 = 13,36  
Centro de custo YYYY = R$29,68 \* 66 / 120 = 16,32

* O sistema somente fará consistência na soma dos percentuais dos rateios fixos para ser igual a 100%, caso o parâmetro "Rateio fixo por valor" NÃO estiver marcado.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412668851607)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412668854935)

* Os Centros de Custos que tiverem a opção **Ativo** desmarcado, ou seja, que estejam inativos, não serão apresentados na tela de cadastro de **Rateios Fixos**:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412652516503)  
  
**Saiba mais**  
[Rateio fixo](https://tdn.totvs.com/display/public/LRM/Rateio+Fixo)
