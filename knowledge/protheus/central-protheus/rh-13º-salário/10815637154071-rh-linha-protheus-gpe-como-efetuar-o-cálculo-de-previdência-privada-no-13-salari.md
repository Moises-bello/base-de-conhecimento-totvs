---
article_id: 10815637154071
category: RH - 13º salário
content_hash: f36213a6e9a2128e76ca15a2761d53b8133c66195c879e1a006d73de8b1c5d29
fetched_at: '2026-06-28T22:44:00.630756+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Como efetuar o cálculo de previdência privada no
  13° Salario
type: support-article
updated_at: '2025-08-20T14:11:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10815637154071-RH-Linha-Protheus-GPE-Como-efetuar-o-c%C3%A1lculo-de-previd%C3%AAncia-privada-no-13-Salario
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19193233098391) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como efetuar o cálculo de previdência privada no 13° Salario?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**A Previdência Privada não é uma determinação da CLT, por isso não há uma forma de cálculo automático deste benefício no roteiro 132 no padrão. As opções de lançamento são:  
  
- **Lançamento Manual** - via rotina de Lançamentos Fixos , por Funcionário ou Verba;  
- **Geração de verbas -** Miscelânea - Cálculos - Geração de Verbas.

1. Será necessário criar a verba de Base e Desconto de Previdência Privada de 13º. Acesse: Atualizações / Definições de Cálculo / Verbas (GPEA040) e clique em Incluir;

2. Crie uma verba do Tipo Desconto e sem Identificador de Cálculo.  
No campo "**Cod Corresp." (RV\_CODCORR)** atrele a verba com Identificador de Cálculo 0302.   
Na aba incidências, os campos "**Ref. a 13º" (RV\_REF13)** e **IR (RV\_IR)** devem estar configurados com SIM:  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10814959728023)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10814714500503)

3. A verba com o Identificador de Cálculo 0302 deve ser incluída como Base Desconto e na aba incidências o campo "**Ref. a 13º" (RV\_REF13)** deve estar configurado com SIM e o campo **"IR" (RV\_IR)** deve estar configurado com Não:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10814811550871)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10817634584471)

4. Em seguida realize o lançamento da verba de Desconto Previdência Privada 13° salario, no roteiro 132 (2° Parcela) e Processe o cálculo do 13º Salário:  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10815381636119)  
  
Memória de Cálculo:  
Base de calculo IR = (Soma das verbas 010 /060 /061/ 107 e 109) = 6.769,81 - 783,94 (INSS 13°) - 50.00 (Previd Privada)   
5.935,87 \* 27.5% = 1.632,36 - 869,36 (aliquota) = R$ 763,00 (desconto IR empregado)

**Saiba Mais**  
[RH - 13º salário](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio)  
Essas **documentações** também podem ser acessadas através da **Carolina**, veja como acessar a assistente virtual, via **Protheus** ou central de atendimento: <https://www.youtube.com/watch?v=T7b4zMlphTI>
