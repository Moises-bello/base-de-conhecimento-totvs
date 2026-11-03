---
content_hash: 2dce7ff1b72e1536f68500d5b61263c1d175dc510d8e97eb4778c6ab06e48d62
fetched_at: '2026-06-29T00:09:25.250822+00:00'
page_id: '423938078'
product: rm
source: tdn-rm
title: Validação da Associação do Plano Paralelo para o SPED Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938078
version: 3
---

A associação entre as contas referenciais e as contas contábeis é uma exigência da Receita Federal para a geração do SPED FCONT e em alguns casos para a geração do SPED Contábil.

Esse processo tem como finalidade verificar se todas as contas contábeis cujo campo 'Natureza da Conta para emissão do SPED' tenha sido informado conforme sua natureza e que tenham sido movimentadas no período informado, foram devidamente associadas às contas referenciais da receita, assim como os centros de custos/contas gerenciais utilizados nessas movimentações.

No final do processo será gerado um LOG com várias informações sobre as associações existentes para auxiliá-lo na geração dos arquivos digitais que serão enviados à Receita.

Se desejar que o sistema faça uma verificação também sobre a associação das contas não movimentadas no período, será necessário marcar a opção "*Validar Conta Contábil sem movimentação, que possui o campo 'Natureza da Conta para emissão do SPED' preenchido e não possui associação com Plano de Contas Paralelo"*.

**Atenção**

Para o SPED FCONT, se um centro de custo estiver associado a uma conta contábil no plano paralelo, todas as movimentações que utilizarem esta conta contábil devem, obrigatoriamente, ter o centro de custo preenchido.
