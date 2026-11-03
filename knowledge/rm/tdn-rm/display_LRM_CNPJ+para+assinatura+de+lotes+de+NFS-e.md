---
content_hash: 4751f7294a254d53e3c27931b678b8cacb483577fce1b57c767023e179179322
fetched_at: '2026-06-29T00:10:20.134498+00:00'
page_id: '485880345'
product: rm
source: tdn-rm
title: CNPJ para assinatura de lotes de NFS-e
type: documentation
url: https://tdn.totvs.com/display/LRM/CNPJ+para+assinatura+de+lotes+de+NFS-e
version: 5
---

****CNPJAUT:****Durante as configurações do TSS, o RM irá validar a seguinte regra para o preenchimento do campo CNPJAUT,

**Modelo da NFS-e DFSNET**

1. Caso o campo "CNPJ Assinatura Lote NFS-e", disponível nos parâmetros da NFS-e do TOTVS Gestão de Estoque, Compra e Faturamento em Integrações | Dados Fiscais | Etapa 2 - Ambiente NF-e esteja preenchido o campo CNPJAUT será preenchido com o mesmo;
2. Caso o campo "CNPJ Assinatura Lote NFS-e" estiver vazio, será carregado o CNPJ do cadastro da Filial Matriz, definida nos parâmetros do TOTVS Gestão Fiscal em 03.02 - Apuração de Tributos | Etapa 22 - Filial Matriz do Estabelecimento;

**Observação**: Para versões do sistema acima da 12.1.26  não existe distinção de validação, o sistema irá considerar o CNPJ informado no campo CNPJ Assinatura Lote NFS-e. Estando vazio será gerado com valor zero.

**Modelo da NFS-e Diferente DFSNET**

1. Caso o campo "CNPJ Assinatura Lote NFS-e", disponível nos parâmetros da NFS-e do TOTVS Gestão de Estoque, Compra e Faturamento em Integrações | Dados Fiscais | Etapa 2 - Ambiente NF-e esteja preenchido, o campo CNPJAUT será preenchido com o mesmo;
2. O campo "CNPJ Assinatura Lote NFS-e" estando vazio será gerado com valor zero.

Informações Adicionais

Ao enviar a NFS-e será apresentado o seguinte aviso:

Prezado Cliente,

Foi criado o parâmetro "CNPJ Assinatura Lote NFS-e", o qual pode ser acessado através dos Parâmetros Fiscais por Filial - "Ambiente NF-e". Este CNPJ será utilizado na assinatura do Lote da NFS-e. O campo deve ser preenchido se houver necessidade definida pela prefeitura.

Qualquer dúvida consulte nossa documentação no link:   
<http://tdn.totvs.com/pages/viewpage.action?pageId=502828953>
