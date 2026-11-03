---
article_id: 27006629402263
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: b9d231e13b860f45354ce8006744ccd3643f8462fc2f977b95dc94cef6e6c419
fetched_at: '2026-06-28T22:38:39.666072+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Campo "Sequencia" (C9_SEQUEN)
  gravando caracteres maiúsculos e minúsculos
type: support-article
updated_at: '2025-04-29T18:46:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27006629402263-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Campo-Sequencia-C9-SEQUEN-gravando-caracteres-mai%C3%BAsculos-e-min%C3%BAsculos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27006629374999) Tempo aproximado para leitura: **00:02:30 min****Dúvida** O campo **"Sequencia" (C9\_SEQUEN)** está gravando registros maiúsculos e minúsculos (Exemplo: '**9a'** e '**9A'**), seria uma inconsistência?  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**A gravação do campo **"Sequencia" (C9\_SEQUEN)** agora permite o registro de sequências com letras maiúsculas e minúsculas, pois isso aumenta o limite de sequências para liberações de pedidos.

Com a inclusão de letras minúsculas, o campo passa a considerar 3.844 variações, em vez das 1296 que seriam possíveis apenas com números e letras maiúsculas.

Essa mudança amplia significativamente as variações disponíveis para a numeração.  
  
**Para mais detalhes consulte as documentações do saiba mais (final dessa documentação).**

**Observação:**   
No Banco de Dados, o que faz essa diferenciação de Maiúsculas e Minúsculas é o "**Collation**", caso identifique algum erro por conta dessa mudança, pode significar que o "**Collation**" do banco precisa ser ajustado.

Para saber a configuração de "**Collation**" padrão exigida pela TOTVS para cada tipo de Banco de Dados, consulte a documentação do saiba mais **(final dessa documentação).**

Após a Issue [DSERFAT-29137](https://tdn.totvs.com/pages/releaseview.action?pageId=838206858), após chegar na numeração '9Z', o sistema vai para a numeração '9a', para serem permitidas mais combinações, contudo, já existe a '9A', se não configurado, o sistema pode enxergar '9A' e '9a' como o mesmo, dando até error.log de CHAVE DUPLICADA.

Sequência do **C9\_SEQUEN**:  
![IMAGE2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31750646784023)  
  
Para aumentar também a disponibilidade de sequência no campo "Sequen. (C9\_SEQUEN)", pode-se ativar o parâmetro [MV\_DEL\_PVL](https://tdn.totvs.com/x/K5zjFQ) (Que depura/elimina itens na SC9 depois de faturar)

**Saiba mais:**

[DSERFAT-29137 DT Liberação de Pedido de Venda - Erro de chave duplicada](https://tdn.totvs.com/pages/releaseview.action?pageId=838206858)

[Banco de dados homologados](https://tdn.totvs.com/display/public/PROT/Banco+de+dados+homologados)

[Collation, Character Type e Code Set/Encoding](https://tdn.totvs.com/display/tec/DBAccess+-+Collation%2C+Character+Type+e+Encoding)
