---
article_id: 360050489594
category: RH - Provisão
content_hash: 6353680108ae1e21ed67bde4a647b132ddfa2b4ebfe40a8c81202f4455ded33e
fetched_at: '2026-06-28T22:43:56.774222+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Provisões com Salário e Jornada Reduzidos - Medida
  Provisória 936 (MP-936)
type: support-article
updated_at: '2025-08-21T12:46:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050489594-RH-Linha-Protheus-GPE-Provis%C3%B5es-com-Sal%C3%A1rio-e-Jornada-Reduzidos-Medida-Provis%C3%B3ria-936-MP-936
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34341354373015) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**Sistema Calcula indevidamente o Salário do Cabeçalho das Provisões considerando a Redução de Jornada/Salarial referente à Medida Provisória 936 (MP-936).   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Este incidente é apresentando quando a verba de Redução Salarial (Identificador de Cálculo 1397) está configurada para Incorporar o Salário do Funcionário, com isto o sistema considera a redução para compor o valor da verba de Salário Base (Identificador de Cálculo 0318), que é utilizado para montagem do Salário no Cabeçalho da Provisão.  
  
De acordo com a MP-936, o valor do Salário-Hora do funcionário deve ser preservado, portanto, o Salário do funcionário no cálculo das provisões não deverá considerar o valor da Redução Salarial.

Para solucionar este erro, realize os seguintes passos:  
  
1. Verifique se o Período da Folha de Pagamento ainda está Aberto;   
2. Se estiver aberto acesse: Atualizações / Definições de Cálculo / Verbas / Localize a Verba com Id de Cálculo 1397 e clique em Alterar;   
3. Altere o campo "**Incorp Sal?**" (RV\_INCORP) para N, e clique em Confirmar;  
4. Reprocesse o cálculo da Folha de Pagamento dos funcionários e verifique se a verba com Identificador de Cálculo 0318 apresenta o Salário Base do funcionário correto, sem considerar a redução Salarial;  
5. Exclua o Cálculo das Provisões dos funcionários. Para saber como excluir o cálculo das provisões [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036636774-MP-GPE-Como-Excluir-o-C%C3%A1lculo-das-Provis%C3%B5es-de-F%C3%A9rias-e-13%C2%BA-Sal%C3%A1rio);  
6. Processe novamente o Cálculo das Provisões de 13º Salário e Férias.  
  
**Observação:** Caso o Período da Folha de Pagamento já esteja Fechado, a alteração no cadastro da verba deverá ser realizada, porém o sistema apresentará o salário integral do funcionário no cálculo das provisões somente no próximo processo de provisão.  
  
A reabertura do período também poderá ser realizada para correção deste erro.   
Para saber como realizar a reabertura de período, acesse: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017683991-MP-GPE-Orienta%C3%A7%C3%A3o-sobre-Reabertura-de-Folha-de-Pagamento>
