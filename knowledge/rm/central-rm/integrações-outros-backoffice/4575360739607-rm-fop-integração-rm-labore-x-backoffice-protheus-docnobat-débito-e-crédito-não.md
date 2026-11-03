---
article_id: 4575360739607
category: Integrações Outros BackOffice
content_hash: a535356c4f3030943ad50e31dac24a682b6fe3887de0e8865fff3e4899fcff10
fetched_at: '2026-06-28T22:46:42.170410+00:00'
product: rm
section_id: 4410716084503
source: central-rm
title: RM - FOP - Integração RM Labore x BackOffice Protheus - DOCNOBAT Débito e Crédito
  não batem
type: support-article
updated_at: '2025-02-10T17:29:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4575360739607-RM-FOP-Integra%C3%A7%C3%A3o-RM-Labore-x-BackOffice-Protheus-DOCNOBAT-D%C3%A9bito-e-Cr%C3%A9dito-n%C3%A3o-batem
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:04:23 min****Ocorrência**Quando no módulo da Folha de Pagamento tentamos integrar o lote contábil com o Protheus é apresentada a seguinte mensagem: 'AJUDA:DOCNOBAT  
O Lançamento / Documento Contábil em questão não está batido (Débito e Crédito não batem!). Este lançamento não poderá ser confirmado!'  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões

**Causa**Este incidente ocorre por divergência nos valores contabilizados para as contas crédito e débito ou pela sobrecarga da informação transmitida ao Protheus.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

1. Verifique se os valores para conta Crédito e Conta Débito estão idênticas ao gerar o lançamento contábil no RM, essa verificação pode ser feita após gerar o lançamento na aba Debug da rotina.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4575220783255/mceclip0.png)

2. Caso estejam divergente os valores, deverá verificar o que foi selecionado para ser contabilizado podendo ser eventos ou encargos.

* Para eventos acesse **Administração de Pessoal | Eventos | Eventos**, edite o evento e verifique em Dados Contábeis se as conta Crédito e Débito estão devidamente preenchidos.
* Para encargos acesse **Encargos | Cadastro | Encargos**, edite o encargo e verifique em Dados Contábeis se as conta Crédito e Débito estão devidamente preenchidos.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4575267869719/mceclip1.png)

3. Caso a conta crédito e conta débito estejam de acordo e os valores idênticos mesmo assim poderá ocorrer o erro.

Nesse caso há uma sobrecarga nas informações que estão sendo enviadas ao Protheus quando o lote contém muitos registros a serem integrados.

Acesse **Configurações | Parametrizador | Integrações | 06.02.06 - Outros Backoffice** e altere o parâmetro "**Qtde. partidas contábeis enviadas por pacote contábil"** para um valor menor do que já está informado.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4575331448087/mceclip3.png)

Foi criado também o parâmetro **"Gravar lote separado por filial"** na rotina de contabilização, assim o lançamento terá um número menor de registros para serem informados ao Protheus, o lote será gerado separado para cada filial.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4575318686615/mceclip4.png)
