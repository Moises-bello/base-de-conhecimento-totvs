---
article_id: 360026463573
category: GPE - eSocial - Não Periódicos
content_hash: 67591254b909723844f3f6164c594655f6f5b5685311f596cbed52ccb647b7df
fetched_at: '2026-06-28T22:45:06.078624+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2399 - Como calcular e integrar rescisão
  para trabalhador sem vínculos através da rotina de Rescisão do SIGAGPE
type: support-article
updated_at: '2023-02-28T21:36:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026463573-RH-Linha-Protheus-GPE-eSocial-S-2399-Como-calcular-e-integrar-rescis%C3%A3o-para-trabalhador-sem-v%C3%ADnculos-atrav%C3%A9s-da-rotina-de-Rescis%C3%A3o-do-SIGAGPE
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:05:00 min  
  
Dúvida**Como calcular e integrar rescisão para trabalhador sem vínculos (autônomo/pro labore) através da rotina de Rescisão do SIGAGPE?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**É possível utilizar a rotina de **cálculo de Rescisão do GPE (GPEM040)** para calcular a rescisão de Trabalhadores Sem Vínculo (Contribuintes Individuais e etc), porém, para isso é necessário que realize os seguintes passos:  
O **Protheus** **não possui um tratamento padrão** para a execução do cálculo da rescisão de Trabalhador Sem Vínculo, uma vez que tal não possui vínculo empregatício e embasamento jurídico, portanto, a Totvs não se responsabilizará pela geração de verbas incorretas no cálculo da rescisão.  
Sendo assim, este documento demonstra a possibilidade do cliente executar o procedimento para atender a sua necessidade.  
Para realizar o cálculo da rescisão de um Trabalhador Sem Vínculo, favor seguir os seguintes passos:  
  
**Passo 1:** Cadastre um período com o roteiro RES para o processo vinculado a esse Trabalhadores Sem Vínculo e certifique-se que o período esteja ativo, **vide exemplo abaixo**: **![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040966934/mceclip0.png)** **Passo 2:** No menu do GPE acesso **Atualizações > Definições Cálculo > Manutenção Tabelas** e cadastre na tabela **S043 - Tipo de Rescisão** um motivo de rescisão condizente com o esse Trabalhadores Sem Vínculo, vale ressaltar que há informações que dispensam o preenchimento devido não existir uma específico ou não ser necessário para essas categorias, **vide exemplo abaixo**:  
  
**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040967114/mceclip1.png)**

**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040967554/mceclip3.png)****Passo 3:** Na rotina de **cálculo de Rescisão do GPE (GPEM0040)** basta selecionar o Tipo de Rescisão desejado e demais campos obrigatórios. O resultado do cálculo será de acordo com as definições preenchidas na tabela **S043 - Tipo de Rescisão**, de acordo com a categoria do Trabalhador Sem Vínculo e de acordo com a configuração das verbas informadas no cálculo, **vide exemplo abaixo**:  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040967794/mceclip4.png)  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040968454/mceclip5.png)  
  
**Observação:** Caso a **categoria do Trabalhador seja 721**, ao gravar o cálculo da rescisão mencionado acima o sistema vai gerar um evento **S-2399** com as Verbas/Rubricas apresentadas no cálculo da mesma forma que é gerado no evento S-2299, para as demais categorias de trabalhadores sem vínculo o evento **S-2399** será integrado sem as verbas rescisórias. Para esses trabalhadores deverá ser gerado o evento S-1200 através da rotina de geração dos eventos periódicos.  
  
Essa tratativa está de acordo com o MOS S-1.1, no evento S-2399 (Trabalhador Sem Vínculo de Emprego/Estatutário - Término), a informação relativa às verbas rescisórias devidas deve ser prestada, neste evento, no grupo  
[verbasResc] apenas em relação aos diretores não empregados com FGTS - categoria [721]. **Nos**  
**demais casos,** **as verbas rescisórias devidas devem ser informadas nos eventos S-1200 ou S-1202,**  
**conforme o regime previdenciário do trabalhador.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12755278970519)**  
  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)   
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
