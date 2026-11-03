---
article_id: 360048215353
category: RH - FGTS / SEFIP
content_hash: 20a1ce2b486499577183cb7fbd2be5f7e848730345a98113759b97fc29c9375d
fetched_at: '2026-06-28T22:43:41.498198+00:00'
product: protheus
section_id: 360003115651
source: central-protheus
title: RH - Linha Protheus - GPE - SEFIP -Rescisão complementar após 2 meses do desligamento
type: support-article
updated_at: '2021-07-17T03:18:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048215353-RH-Linha-Protheus-GPE-SEFIP-Rescis%C3%A3o-complementar-ap%C3%B3s-2-meses-do-desligamento
---

**Dúvida**

 A SEFIP para rescisão complementar, dois meses após a rescisão original,  está pagando o FGTS  recolhido na GRRF.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17.

**Solução:**

O SEFIP só recebe movimentação com data dentro do mês de competência, mês anterior ou posterior a data de demissão. É no registro de movimentação onde é informado ao SEFIP que o FGTS já foi recolhido. Como o SEFIP possui essa limitação, o Microsiga Protheus não gera a Movimentação, para não apresentar a inconsistência:  
  
**320649 – Para movimentação I1, I2, I3, I4 ou L a data de movimentação deve ser informada no mês da****competência, mês anterior ou mês posterior.**

Com isso, o SEFIP não tem a informação que o **FGTS já foi recolhido** e gera o recolhimento novamente.  
**Este é um problema do SEFIP.**

Para contornar este problema há duas formas:  
  
**Primeira**:  
- Gere o SEFIP de todos os funcionários do mês normalmente e na pergunta Gerar Rescisão Comp?informe A Pedido. Desta forma os funcionários da rescisão complementar não serão considerados.  
- Faça a importação para o programa do SEFIP.  
- Depois, gere outro SEFIP e informe Por Dispensa, na pergunta Gerar Rescisão Comp?.  
- Informe SIM, para a pergunta Somente Resc. Complementar, e na pergunta Modalidade, informe Declaração.  
- Após isso, importe o novo arquivo. Por ser modalidade Declaração não irá sobrepor o primeiro arquivo importado que se trata de Recolhimento.  
- O SEFIP não calculará valor de FGTS já recolhido na GRRF, porém não calculará o INSS sobre 13º salário, pois o SEFIP também só recebe valores de 13º salário em dezembro ou quando há movimentação definitiva.  
**Segunda:**- Alterar a data de demissão do funcionário no cadastro de funcionários para um mês antes da geração do SEFIP e gerar o SEFIP normalmente. Desta maneira, o Sistema irá gerar um registro de movimentação informando que o FGTS foi devidamente recolhido, não gerando pagamento em duplicidade. Após isso é necessário fazer uma retificação a CEF da data de movimentação e restaurar data de demissão no cadastro de funcionários.  
  
**Importante**: Os procedimentos acima são paliativos para contornar uma inconsistência do programa SEFIP. Em nenhuma das formas o SEFIP fica 100% correto e não existe outra maneira, por se tratar de uma deficiência do sistema SEFIP. Estes procedimentos foram adotados por se tratar de um assunto de grande demanda e porque alguns de nossos clientes receberam em algum momento estas instruções diretamente de atendentes da CEF, como única maneira de enviar os dados e retificá-lo  
  
Saiba mais: <https://tdn.totvs.com/display/public/PROT/FGTS>
