---
article_id: 360028866271
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 18632ca4771f9b8bf0fdb90e3cf8a50ef5ed237f781293d955d74915896a3898
fetched_at: '2026-06-28T22:40:45.738679+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACTB - ECD registro
  J005 - VL_CTA_INI / IND_COD_AGL e IND_GRP_BAL
type: support-article
updated_at: '2026-04-24T14:49:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028866271-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACTB-ECD-registro-J005-VL-CTA-INI-IND-COD-AGL-e-IND-GRP-BAL
---

Ao validar a ECD, ocorre erro de divergência entre saldos iniciais do Ativo e Passivo no balanço patrimonial. Para corrigir, revise o plano de contas, visão gerencial, naturezas das contas, atualize procedures, pacotes e valide a geração do arquivo, ajustes nas configurações da visão e cadastros contábeis, garantindo que saldos e níveis estejam corretos conforme normas.

**Ocorrência**  
Ao realizar a validação da ECD, apresenta os erros abaixo:  
  
*"No Balanço Patrimonial, o somatório do saldo inicial (J100 VL\_CTA\_INI) das linhas de detalhes (J100 IND\_COD\_AGL="D") do Ativo (J100 IND\_GRP\_BAL="A") está diferente do somatório do saldo inicial (J100 VL\_CTA\_INI) das linhas de detalhe (J100 IND\_COD\_AGL =") do Passivo (J100 IND\_GRP\_BAL="P")."*

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029576471)

*"No Balanço Patrimonial, o valor do saldo inicial do último nível do Ativo deve ser igual ao valor do saldo inicial do último nível do Passivo e Patrimônio Líquido.'*

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029577912)

**Ambiente**  
Microsiga Protheus – Contabilidade Gerencial – A partir da versão 11  
  
  
**Solução**  
Para corrigir a divergência de saldos no registro J005 da ECD, é necessário revisar a estrutura do plano de contas, configurações da visão gerencial, naturezas das contas e garantir que o ambiente esteja devidamente atualizado com as últimas rotinas, pacotes e procedures.  
  
**Passos:**

1. Realize a conciliação do bloco J100 e compare se o saldo está correto em relação ao relatório de balanço gerado no Protheus.  
   [Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBS001 - ECD Registro J100](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023992791-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECD-Registro-J100?source=search)
2. Verifique se as procedures estão devidamente atualizadas:  
   [Cross Segmento - Backoffice Linha Protheus - SIGACTB - SIGAATF - SIGAPCO - Procedure Desatualizada ou Incompatível](https://centraldeatendimento.totvs.com/hc/pt-br/articles/30076556464023-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-SIGAATF-SIGAPCO-Procedure-Desatualizada-ou-Incompat%C3%ADvel)
3. Verifique a atualização e aplicação dos pacotes Backoffice, LIB e DBAccess pertinentes à sua versão.  
   [Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBS001 - Pacote de atualização e como realizar a atualização da ECD 2026 (leiaute 9)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025142372-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-Pacote-de-atualiza%C3%A7%C3%A3o-e-como-realizar-a-atualiza%C3%A7%C3%A3o-da-ECD-2026-leiaute-9?source=search)
4. Veja todos os pontos aqui descritos:  
   [Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECD registro J150 - 7-VL\_CTA e 2-COD\_AGL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028548031-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-registro-J150-7-VL-CTA-e-2-COD-AGL?source=search)
5. Valide a geração do arquivo verificando se o passivo está sendo gerado com a indicação "P" e o ativo com a indicação "A".

   ![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029574471)
6. Verifique se está correto ser gerado igual a "D" ou deveria gerar "C".
7. Verifique se a situação ocorre somente para alguma conta "Conta Inicial e Conta Final" específica, exemplo: conta depreciação acumulada redutora do Ativo.
8. Acesse o cadastro da visão gerencial (CTBA161), e verifique se o campo "Identific" no cadastro da visão está configurado como "subtrai"; neste caso, deve ser alterado para "soma" e um novo teste de geração deve ser realizado.

   ![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029790551)
9. Confirme no cadastro da Visão se a "Cond Normal" foi informada com a mesma natureza presente no cadastro da conta contábil correspondente.

   ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029790291)
10. No cadastro da Visão Gerencial, não informe o campo "Fórmula".
11. Verifique se existe algum centro de custo amarrado à visão de balanço. Realize um teste desamarrando o centro de custo e gerando uma nova revisão.

    ![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029800752)
12. Acesse o cadastro da conta contábil e valide se a natureza da conta está correta (exemplo: Dedutora). Após eventuais ajustes, gere a revisão e compare se o saldo J100 é gerado de forma correta com o relatório de balanço.
13. Verifique se o nível de aglutinação criado na Visão Gerencial segue o mesmo conceito do plano de contas – Registro I050.  
      
    [Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECD I050 : 5 - NIVEL O plano de contas com todas as suas contas sintéticas e analíticas deve conter no mínimo 4 níveis (Resolução CFC 1299/2010).](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028148692-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-I050-5-NIVEL-O-plano-de-contas-com-todas-as-suas-contas-sint%C3%A9ticas-e-anal%C3%ADticas-deve-conter-no-m%C3%ADnimo-4-n%C3%ADveis-Resolu%C3%A7%C3%A3o-CFC-1299-2010?source=search)

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029574531)
