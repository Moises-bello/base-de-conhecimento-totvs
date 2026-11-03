---
article_id: 1500006060961
category: Gestão Ambiental (SIGASGA)
content_hash: 55bcb01e9ea0c5f55f0331e17e406472d23b9c3066fe07b489240f95c5043a7d
fetched_at: '2026-06-28T22:42:38.464433+00:00'
product: protheus
section_id: 360012117893
source: central-protheus
title: 'Manufatura - Linha Protheus - SGA - Resíduos e Disposição Final - Integração
  SGA x Estoque '
type: support-article
updated_at: '2021-08-30T16:44:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006060961-Manufatura-Linha-Protheus-SGA-Res%C3%ADduos-e-Disposi%C3%A7%C3%A3o-Final-Integra%C3%A7%C3%A3o-SGA-x-Estoque
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png)** Tempo aproximado para leitura: **00:01:45 min****Dúvida**Como funciona a integração do módulo de **Gestão Ambiental - SGA** com o **Estoque - SIGAEST** quanto ao **Resíduo** e a **Disposição Final**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) – Gestão Ambiental (SIGASGA) – Versão 12  
  
**Solução**O módulo de **Gestão Ambiental - SGA** possui integração com o módulo de **Estoque**, gerando informações nas tabelas de **Saldo do Produto -** **SB2** e **Movimentações -** **SD3**. Após a implementação da rotina de **Disposição Final - SGAA531**, ao realizar o fluxo de saída de resíduos no momento de uma inclusão de uma disposição final, o Sistema faz uma retirada na **SB2** e registra uma movimentação de saída na **SD3**. Caso a disposição final seja excluída, o resíduo retorna para o armazém.  
  
Para melhor entendimento, segue um exemplo:  
  
1. Incluir uma **Classe não Perigosa**:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008042982/mceclip0.png)

2. Incluir um **Resíduo**:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008043042/mceclip1.png)

3. Incluir uma **Definição de Resíduos** para o **Resíduo**:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008043142/mceclip2.png)

4. Incluir duas **Ocorrências**:  
Ocorrência **000028**:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008223201/mceclip3.png)

Ocorrência **000029**:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008223281/mceclip4.png)

5. No módulo do **Estoque**, acessar a rotina de **Saldo Atual - MATA225**, verificar que as quantidades definidas nas duas ocorrências foram somadas:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008223321/mceclip5.png)

6. Acessar a rotina de **Movimentação Simples - MATA240** e verificar os dois registros incluídos:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008043502/mceclip6.png)

7. Incluir uma **Disposição Final - SGAA531** para uma das **Ocorrências**:

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008223381/mceclip7.png)

8. Verificar que o **Saldo Atual - MATA225** do **Resíduo** diminuiu:

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008223481/mceclip8.png)

9. Verificar que nas **Movimentação Simples -** **MATA225**, houve um novo registro de **Tipo Movimento** igual a **999**:

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008223561/mceclip9.png)

10. Realizar a exclusão da**Disposição Final -** **SGAA531**:

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008223601/mceclip10.png)

11. Verificar que o estoque foi acrescido novamente, pois, o resíduo que havia **Saído**, com a exclusão do registro, ele **Retornou** ao estoque:  
**Saldo Atual - MATA225**

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008223661/mceclip11.png)

**Movimentação Simples - MATA240**

**![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008223681/mceclip12.png)**
