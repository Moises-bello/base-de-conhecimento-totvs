---
article_id: 360047397513
category: eSocial - Cadastros
content_hash: 766b960e915a3fa5c97667da43c6c7cc92d66f89706826fd876e929595f46f63
fetched_at: '2026-06-28T22:47:14.593591+00:00'
product: rm
section_id: 1500000834341
source: central-rm
title: RM - eSocial - MP 936 - Redução proporcional de jornada de trabalho e salário
  - Geração S-2206
type: support-article
updated_at: '2021-03-31T17:23:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047397513-RM-eSocial-MP-936-Redu%C3%A7%C3%A3o-proporcional-de-jornada-de-trabalho-e-sal%C3%A1rio-Gera%C3%A7%C3%A3o-S-2206
---

**Dúvida**  
Como informar a redução de salário e jornada do funcionário decorrente da **Medida Provisória 936**?  
  
**Ambiente**  
RM - eSocial - A partir dos *Patches* 12.1.25.271, 12.1.26.217, 12.1.27.173 e 12.1.28.107  
  
**Solução**  
Quando o funcionário tiver redução de salário e jornada devido à MP 936, o empregador deve enviar um evento de alteração contratual (**S-2206**) com **Data de Alteração** igual ao **início do período de redução de salário e jornada.** Neste evento, deve informar também o valor do salário reduzido, a nova jornada a ser cumprida pelo trabalhador durante esse período e, no campo observação, deve informar o prazo pactuado para a referida redução e o percentual definido para essa redução proporcional.

Para geração do **S-2206 - Alteração de Contrato de Trabalho**, siga os passos abaixo:

1. No módulo TOTVS Folha de Pagamento acesse o menu **Administração de Pessoal | Funcionários**;  
2. Edite o funcionário em desejado e acesse o menu lateral **Informações Contratuais | Registro**;  
3. Selecione a aba **B.E.M** e preencha as informações.

Acesse [Cadastro e geração do Benefício Extraordinário Mensal - B.E.M.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047351593) para informações detalhadas sobre o cadastro.

O gatilho do **S-2206** só será gerado quando no cadastro supracitado for preenchido o tipo de adesão **Redução da carga horária**. Caso o preenchimento dos campos do cadastro B.E.M. seja pelo processo global, somente será gerado gatilho caso o campo **Data do acordo** seja cadastrada.  
  
**Importante**  
O cadastro do B.E.M. **não irá alterar os valores de salário e jornada do cadastro do funcionário** pois outros processos do sistema utilizarão o salário cheio para processamento. Os dados da redução serão apresentados **somente no XML e no histórico** do B.E.M..

Caso os campos do cadastro B.E.M já tenham sido preenchidos **antes** das versões 12.1.25.268, 12.1.26.212, 12.1.27.166 e 12.1.28.102 será necessário a geração do gatilho do evento **S-2206 - Alteração de Contrato de Trabalho** manualmente para o funcionário ou pelo processo [Gerar Gatilhos em Lotes](https://tdn.totvs.com/display/LRM/Gerar+Gatilhos+em+Lotes) para uma seleção de funcionários (a data de alteração no processo deverá ser igual a data do acordo cadastrada).

Conforme orientação do eSocial, após o período do acordo B.E.M. é necessário o envio do evento de alteração contratual (**S-2206**) atualizado as informações novamente de salário e jornada do funcionário. Este gatilho ocorrerá de forma automática na liberação de competência a partir das versões indicadas acima na área **Ambiente**.  
  
**Saiba mais**  
Para verificar formas de pagamento e outros detalhes sobre a redução da jornada e salário, acesse:  
      • [MP 936 - Redução Proporcional de Jornada de Trabalho e Salário](https://tdn.totvs.com/pages/releaseview.action?pageId=545621517)  
      • [MP 936 - Redução de Jornada de Trabalho (Automação Ponto)](https://tdn.totvs.com/pages/releaseview.action?pageId=545257629)
