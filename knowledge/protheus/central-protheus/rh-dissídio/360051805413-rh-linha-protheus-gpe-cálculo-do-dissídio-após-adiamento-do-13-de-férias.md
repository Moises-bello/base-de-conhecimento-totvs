---
article_id: 360051805413
category: RH - Dissídio
content_hash: 0bb6aad7ceeae86d55d33f0198fd97d3a65c56a87724c4be14a69345827ff955
fetched_at: '2026-06-28T22:43:43.513292+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo do dissídio após adiamento do 1/3 de férias
type: support-article
updated_at: '2025-08-20T15:21:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051805413-RH-Linha-Protheus-GPE-C%C3%A1lculo-do-diss%C3%ADdio-ap%C3%B3s-adiamento-do-1-3-de-f%C3%A9rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34318884052375) Tempo aproximado para leitura: **00:01:00 min**  
**Ocorrência**Cálculo do dissídio após adiamento do 1/3 de férias.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12  
  
**Causa**Foi efetuado o procedimento para adiar o pagamento do 1/3 de férias no cálculo de férias do funcionário, conforme documentação disponível [aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045596313). Ao efetuar o cálculo do dissídio de funcionário com cálculo de férias que ocorreu antes do período de início do adiamento do 1/3 de férias, não ocorre apuração correta da diferença de 1/3 de férias. **Solução**

Para tratar os casos de cálculo no dissídio, foi efetuado alteração nas fórmulas padrão de geração de 1/3 nas férias (**S\_GRTERFER** e **S\_GRTERABO**) para verificar se o cálculo das férias foi realizado dentro do período do adiamento de 1/3 de férias ou se foi realizado antes do adiamento ou após o término do adiamento.

**Atenção**

Como houve alteração nas fórmulas padrão, o roteiro **FER** deverá ser alterado manualmente no cadastro de roteiros para **habilitar** a execução das fórmulas **S\_GRTERFER** e **S\_GRTERABO**; por consequência, as fórmulas de usuário criadas na documentação disponível [aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045596313) **não** precisarão ser mais utilizadas, então também deve ser efetuado alteração no roteiro **FER** para **desabilitá-las.**Para permitir o controle automático citado acima, foram criados **mnemônicos** em que deverão ser preenchidos as informações referente ao período inicial e final do adiamento do 1/3 de férias e aos códigos das verbas de base que foram criados para demonstrar o valor do 1/3 de férias adiado:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079509374)  
Com a configuração do exemplo acima, foi definido para o sistema que o período de adiamento do 1/3 de férias ocorre entre **03/2020** a **11/2020**, a geração do valor de 1/3 de férias será realizado nas verbas de códigos **MP1** e **MP2** e a geração do valor de 1/3 de abono será realizado nas verbas de códigos **MP3** e **MP4**.  
  
**Dica**

Caso não tenha adiamento do 1/3 de abono, não informe os códigos da verba nos mnemônicos P\_ADIUTAM e P\_ADIUTAMS, pois dessa forma o sistema fará a geração desse valor nos Ids de cálculo padrão (0079 e 0206).

Caso não tenha o adiamento de 1/3 de férias para nenhum funcionário, basta não preencher nenhum dos mnemônicos acima, pois dessa forma o sistema fará a geração de 1/3 de férias nas verbas de Ids de cálculo padrão (0077, 0078, 0079 e 0206).

Seguindo a configuração do exemplo acima, se for efetuado cálculo de férias com início em 07/2020, como o período estará compreendido no adiamento do 1/3 de férias, a rotina irá gerar o 1/3 de férias nas verbas de base MP1 e MP2. Se for efetuado o cálculo de férias com início em 12/2020, não será realizado o adiamento do 1/3 e o sistema irá gravar o 1/3 nas verbas relacionadas aos Ids de cálculo padrão (0077, 0078, 0079, 0206).

Para o dissídio, o sistema seguirá a mesma lógica das férias: se no período houver férias com início antes do período de adiamento de 1/3 de férias, o sistema irá apurar o 1/3 nas verbas dos Ids de cálculo padrão (0077, 0078, 0079, 0206); caso o férias tenha início após o período de adiamento de 1/3 de férias e antes do período de término, o sistema fará uma busca adicional na tabela SRR para verificar se no cálculo das férias foi gerado a verba de base de 1/3 de férias/abono para somente assim considerar que a geração do 1/3 de férias/abono deve ser efetuado nas verbas de base, uma vez que pode haver possibilidade do funcionário não ter tido o 1/3 de férias adiado, mesmo após o período de início do adiamento, por alguma regra específica da empresa.  
  
**Importante**

Para que uma verba seja recalculada no dissídio, é necessário que o campo **"Dissid. Ret." (RV\_COMPL\_)** esteja preenchido com "**S**" (Sim) e ainda é necessário preencher o código da verba onde será gerado a diferença de dissídio no campo **"Verba P.Diss" (RV\_CODCOM\_)**, ambos disponíveis no cadastro de verbas.

Caso no período de cálculo do dissídio ainda não seja devido o pagamento da diferença do 1/3 de férias, ou seja, o pagamento também será adiado, recomenda-se a criação de mais verbas de base para que seja gravado a diferença de 1/3 de férias nessas verbas. Com isso, será possível distinguir o valor de 1/3 de férias que é proveniente do cálculo de férias e o valor de 1/3 de férias que é proveniente de diferença gerada no dissídio. Dessa forma, quando for executado o programa **PGTFER927**, de acordo a este [tutorial](https://tdn.totvs.com/x/cvTAI), será necessário preencher tanto os códigos das verbas de 1/3 de férias geradas no cálculo das férias quanto os códigos de diferença de 1/3 de férias gerados no dissídio.

Caso no período de cálculo do dissídio já seja devido o pagamento da diferença do 1/3 de férias, ou seja, esse valor será pago em folha, não será necessário criar novas verbas de verbas, devendo apenas efetuar preenchimento dos campos "Dissid. Ret." (RV\_COMPL\_) e "Verba P.Diss" (RV\_CODCOM\_), onde no último campo poderá ser informado as verbas de diferença de 1/3 de férias padrão (Ids 0090 e 0091) ou outras verbas conforme preferência, pois dessa forma as diferenças serão geradas em verbas de provento, sendo assim pagas na folha do funcionário. Dessa forma, quando for executado o programa **PGTFER927**, de acordo a este [tutorial](https://tdn.totvs.com/x/cvTAI), será necessário preencher apenas os códigos das verbas de base de 1/3 de férias geradas no cálculo das férias.

 

Saiba Mais:  
[Página Centralizadora do Dissídio (GPEM690)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio)
