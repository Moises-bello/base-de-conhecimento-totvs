---
article_id: 360063018633
category: RH - Férias
content_hash: 4aec4a44bbfb5d10a385245afcdb7d78704223df879dfd969987fb8e22cf4358
fetched_at: '2026-06-28T22:43:59.377581+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - O que conferir quando não é executado o cálculo
  das férias
type: support-article
updated_at: '2025-08-21T19:52:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063018633-RH-Linha-Protheus-GPE-O-que-conferir-quando-n%C3%A3o-%C3%A9-executado-o-c%C3%A1lculo-das-f%C3%A9rias
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34354616858263) Tempo aproximado para leitura: 00:02:00 min****Dúvida**O que conferir quando não é executado o cálculo das férias?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para solucionar essa dúvida, verifique as seguintes configurações:  
  
1. **Cadastro do Roteiro:** Atualizações > Definição Cálculo > Períodos  
O roteiro FER deve ser criado para o mês que **inicia as férias e também para o mês que termina.** Por exemplo, férias que iniciam em 10/05/2021 com término em 08/06/2021. Dessa maneira crie o roteiro FER para as competências 05/2021 e 06/2021. O roteiro de FER **não pode estar com data de integração nem data de fechamento**, caso esteja integrado, cancele a integração para depois calcular as férias.   
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101379534)  
  
2. **Tipo de Ausência:** Atualizações > Definição Cálculo > Tipos de Ausência  
O Tipo de Ausência Férias tem que estar criado e com a verba de ID 0072 informada no campo Cod.Verba.  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002540321)  
  
3. **Controle Dias de Direito:** Atualizações > Funcionários > Controle Dias de Direito  
Avalie o controle de dias de direito do funcionário que está tentando calcular as férias. O campo Situação do período aquisitivo em questão deve estar como **Ativo**.  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360103544553)

4. **Cadastro do Funcionário**: Atualizações > Funcionários > Aba Funcionais   
O campo referente ao **salário** deve estar informado, caso esteja em branco o cálculo não é efetuado.   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13606863551895)

**Observação:** Para visualizar as imagens desse artigo em tamanho maior, clique com o botão direito do *mouse* sobre a imagem e selecione Abrir imagem em uma nova guia.

**Saiba Mais**[RH - Linha Protheus - GPE - Como calcular férias na versão 12](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015658231-RH-Linha-Protheus-GPE-Como-calcular-f%C3%A9rias-na-vers%C3%A3o-12)  
[RH - Linha Protheus - GPE - Como cancelar cálculo de férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050830934-RH-Linha-Protheus-GPE-Como-cancelar-c%C3%A1lculo-de-f%C3%A9rias)  
[RH - Linha Protheus - GPE - Como calcular e parametrizar o abono pecuniário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411050216471-RH-Linha-Protheus-GPE-Como-calcular-e-parametrizar-o-abono-pecuni%C3%A1rio-)  
[RH - Linha Protheus - GPE - Como Funciona a Rotina Controle de Dias de Direito](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015671131-RH-Linha-Protheus-GPE-Como-Funciona-a-Rotina-Controle-de-Dias-de-Direito)  
[RH - Linha Protheus - GPE - Ao calcular férias, Sistema traz período aquisitivo ou dias de férias incorreto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017554792-RH-Linha-Protheus-GPE-Ao-calcular-f%C3%A9rias-Sistema-traz-per%C3%ADodo-aquisitivo-ou-dias-de-f%C3%A9rias-incorreto)
