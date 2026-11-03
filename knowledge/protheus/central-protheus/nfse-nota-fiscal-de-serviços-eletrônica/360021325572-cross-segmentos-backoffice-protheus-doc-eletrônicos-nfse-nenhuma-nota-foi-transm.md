---
article_id: 360021325572
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 063b46d938498aa0545a1ad11aa692c74401da7513017e5391088a101bffb543
fetched_at: '2026-06-28T22:39:57.581721+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Nenhuma Nota
  foi Transmitida (Saída)
type: support-article
updated_at: '2026-05-05T10:07:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021325572-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Nenhuma-Nota-foi-Transmitida-Sa%C3%ADda
---

**Ocorrência**  
No módulo **Faturamento**, ao tentar realizar a transmissão de uma **NFSE (Nota de Saída)** pela rotina **FISA022**, é apresentado uma mensagem de erro "**NENHUMA NOTA FOI TRANSMITIDA**".  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - Todas as versões   
  
**Causa**  
Esse incidente ocorre geralmente por erros cadastrais, onde alguns dados não são levados corretamente para alguns campos e consequentemente o XML da nota não é gerado.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
  
**1.** Verifique se a nota gerou registros nas tabelas CD2, SF3 e SFT. Caso não tenha gerado, revise as configurações fiscais;  
  
**2.** Verifique se a espécie do documento está igual a RPS, verificando o parâmetro MV\_ESPECIE e o campo F3\_ESPECIE;  
  
**3.** Verifique se o campo B1\_CODISS está preenchido e se alimentou todos os demais campos filtrando pela nota: C6\_CODISS, D2\_CODISS, F3\_CODISS e FT\_CODISS;  
  
**4.** Verifique se o campo F3\_CFO está preenchido com um código que inicia com 5 ou superior, para caracterizar uma nota de saída;  
  
**5.** Verifique e remova os **caracteres especiais** da discriminação dos serviços e do cadastro do tomador.  
  
**IMPORTANTE**  
**Caso um ou mais itens acima estejam fora do padrão indicado, a equipe Fiscal deverá ser acionada para orientação quanto à correção, visto que são problemas ainda na escrituração da nota.**  
  
Observações:   
Se todos os itens acima estiverem corretos e a mensagem "Nenhuma Nota Transmitida" persistir, existe a possibilidade dessa nota já ter sido transmitida. Para confirmar isso, realize o monitoramento da nota, e se o status estiver pendente, é necessário aguardar o processamento ou verificar se ocorre algum erro no console do TSS.
