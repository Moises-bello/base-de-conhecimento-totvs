---
article_id: 360048735714
category: Rescisão
content_hash: 716e9a96a07ab07f277dab3f5d9b7e8912d8459dd443b51000c1a8869124caab
fetched_at: '2026-06-28T22:46:55.304177+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: RH - RM - FOP - Rescisão por Comum Acordo
type: support-article
updated_at: '2024-06-17T14:17:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048735714-RH-RM-FOP-Rescis%C3%A3o-por-Comum-Acordo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24229851491607)**Tempo aproximado para leitura: **00:05:30 min****Dúvida**Como cadastro uma rescisão do tipo Comum Acordo no sistema?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Existem duas alternativas para se fazer a rescisão por Comum Acordo, a depender do entendimento do usuário.   
  
**Alternativa 1:** Nesta opção, considera-se para o cálculo da projeção em férias indenizadas e 13º salário indenizado como o valor inteiro informado no campo **"Dias de Aviso Indenizado"**. Para realizar a rescisão desta forma, realize os seguintes passos:  
  
1. Selecione o funcionário, acesse o ícone **Rescisão**, e escolha o **tipo de demissão V - Comum acordo**:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072557254)

No campo **Dias de Aviso Indenizado**, deve-se preencher o valor que corresponde à metade do total de dias a serem indenizados. Quando a metade destes dias resultar em decimal, por exemplo, 33 dias de aviso prévio indenizado (onde o valor seria 16,5 dias), o valor a ser inserido no campo deve ser arredondado, no caso deste exemplo, 17 dias. Posteriormente, ao calcular a rescisão, haverá o parâmetro **Aviso Prévio Indenizado abate 0,5 dia**:

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072558394)**

2. Cadastre o restante da rescisão normalmente. Segue abaixo um exemplo:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073735033)

3. Ao salvar e clicar em **Calcular Rescisão**, será apresentada a tela demonstrada no passo 1, onde é possível marcar o flag **Aviso prévio indenizado abate 0,5 dia**. Logo, parametrize de acordo com sua necessidade e avance.  
  
Ao calcular a rescisão, veja o envelope:

![evt_sem_flag.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073735613)

O sistema reconhece a referência de 15 dias de aviso prévio indenizado:

![sem_flag.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072559534)

**Alternativa 2:** Neste caso, o usuário entende que não deve pagar o avo indenizado de férias e 13º sobre a metade do aviso prévio indenizado, e que portanto apenas o aviso prévio indenizado deve ser pago pela metade, conforme prevê a rescisão do tipo Comum Acordo. Para realizar a rescisão desta forma, realize os seguintes passos:  
  
1. Acesse **Configurações | Parametrizador | Rescisão | Aviso Prévio** e marque o flag **Comum Acordo** **paga metade somente do aviso prévio. Projeções consideram período completo**.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073738413)

2. Com o parâmetro acima marcado, ao cadastrar a rescisão por Comum Acordo, deve-se preencher, portanto, o valor total de dias a serem indenizados, diferente da primeira alternativa.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072563854)

3. Prossiga com a rescisão normalmente. Ao calcular, repare que, diferente da primeira alternativa, a referência para o evento de provento de Aviso Prévio Indenizado fica como 30, conforme preenchido no campo **Dias de Aviso Indenizado**, ao cadastrar a rescisão:

![evt_com_flag.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072564134)

Perceba que o valor pago é o mesmo.

Ambos os exemplos são com o mesmo salário. O que modificou-se foi apenas o comportamento do código de cálculo diante da flag marcada no parametrizador. Veja:

![com_flag.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073739153)

Por fim, como padrão para ambas as alternativas acima, será pago 50% do valor do Aviso Prévio Indenizado (de acordo com o já exposto acima), e 20% para a multa rescisória.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072564574)

Veja o cálculo do evento de código de cálculo 28:

![evt_fgts_artigo_22.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073739833)

FGTS Quitação + FGTS 13º Rescisão + Saldo FGTS no Banco = Multa Rescisória \* 20% = Valor do Evento  
  
No exemplo:

107,52 + 44,80 + 2.000,00 = 2152,32 \* 20% = 430,46  
  
**Legislação:**  
Art. 484 - A. O contrato de trabalho poderá ser extinto por acordo entre empregado e empregador, caso em que serão devidas as seguintes verbas trabalhistas:  
I – por metade:  
a) o aviso prévio, se indenizado; e  
b) a indenização sobre o saldo do Fundo de Garantia do Tempo de Serviço, prevista no § 1º do art. 18 da Lei nº 8.036, de 11 de maio de 1990;  
II – na integralidade, as demais verbas trabalhistas.  
§ 1º A extinção do contrato prevista no caput deste artigo permite a movimentação da conta vinculada do trabalhador no Fundo de Garantia do Tempo de Serviço na forma do inciso I-A do art. 20 da Lei nº 8.036, de 11 de maio de 1990, limitada até 80% (oitenta por cento) do valor dos depósitos.  
§ 2º A extinção do contrato por acordo prevista no caput deste artigo não autoriza o ingresso no Programa de Seguro-Desemprego.
