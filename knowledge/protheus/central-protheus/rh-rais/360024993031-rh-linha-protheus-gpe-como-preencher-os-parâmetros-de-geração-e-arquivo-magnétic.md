---
article_id: 360024993031
category: RH - RAIS
content_hash: 79ecd893307f20c6bd4b2a3a52decc35702cc0567117414ec5bc05654399f182
fetched_at: '2026-06-28T22:44:05.748178+00:00'
product: protheus
section_id: 360000030327
source: central-protheus
title: RH - Linha Protheus - GPE - Como preencher os parâmetros de geração e arquivo
  magnético da RAIS
type: support-article
updated_at: '2022-04-07T13:32:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024993031-RH-Linha-Protheus-GPE-Como-preencher-os-par%C3%A2metros-de-gera%C3%A7%C3%A3o-e-arquivo-magn%C3%A9tico-da-RAIS
---

**Dúvida**Como preencher os parâmetros de geração (GPEM500) e arquivo magnético (GPEM530) da RAIS?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 11.  
  
**Solução**  
1. Parâmetros importantes na geração de valores: Miscelânea/ RAIS/Geração do Arquivo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023396611/mceclip1.png)

**Ano Base?** Informe o Ano Base que deseja efetuar a geração do Arquivo da RAIS. No caso 2018;   
**Centralizar na Fil.?** Se este campo for preenchido, todos os funcionários serão centralizados na filial preenchida, que é a responsável por todas as informações geradas;  
**Gerar Por CEI?** Se o arquivo será gerado por centro de custo CEI;  
**Verbas de Comissão? / Continuação?** Esses campos definem as verbas que serão consideradas para compor o salário do comissionado;  
**Comis. com Sal Zero?** Define se para o comissionado puro, o calculo será realizado sobre a remuneração do mês ou sobre as verbas informadas;  
**Cons. Media Comis.?** Define se irá ser considerado as médias de comissão para compor o salário contratual, independe da categoria do funcionário;  
**Projeta Data de Demissão?** Influenciará diretamente na apresentação das verbas de rescisão na manutenção arquivo.

2. Parâmetros importantes na geração do arquivo magnético: Miscelânea/ RAIS/ Arquivo Magnético:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023357952/mceclip3.png)

**Filial Responsável?** Este campo define qual filial será responsável pelas informações;        
**Ano de Declaração?** Informe o Ano Base que deseja efetuar a geração do Arquivo da RAIS. No caso 2018;  
**Path Arquivo Saída?** Caminho onde o arquivo será gravado. Se não for informado o caminho correto ou se o usuário que está gerando o mesmo não tiver acesso a pasta informada é exibido o erro DOS: 430. **Exemplo de preenchimento**: C:\RAIS\RAIS.TXT  
**CNPJ centralizadora?** Preencher este campo somente se houver o pagamento da contribuição sindical de forma centralizada  
**Considera Afastado s/Remun?** Este campo define se funcionários sem remuneração no ano base serão gravados no arquivo  
  
**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4423782740631/mceclip0.png)Precisa de ajuda na realização dos processos de geração e conferência da RAIS? Assista os vídeos *How To abaixo*e tire suas dúvidas:**  
  
-Geração Arquivo

-Geração arquivo magnético  
  
  
**Saiba Mais**Para mais informações acesse o *link* a seguir: <http://tdn.totvs.com/x/DpjHEw>
