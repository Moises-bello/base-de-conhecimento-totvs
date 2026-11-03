---
content_hash: 6229e0a8cc46d2c020d2b0788f050a2f9c634043acff5296d13ed4f0d64e1cbd
fetched_at: '2026-06-29T00:09:31.737042+00:00'
page_id: '425458700'
product: rm
source: tdn-rm
title: Incluir Bolsas
type: documentation
url: https://tdn.totvs.com/display/LRM/Incluir+Bolsas
version: 3
---

---

O processo de inclusão de bolsas, tem a opção de selecionar múltiplas bolsas para serviços diferentes, não sendo mais preciso efetuar o processo toda vez que for efetuar a inclusão para um determinado serviço, em um único processo é possível incluir uma bolsa para vários Serviços do Aluno.  
Este processo encontra no Assistente em Financeiro/Contábil ( Incluir Bolsa ) e só é possível para executar o processo para alunos que já possuem contratos.

**Observação:**   
No TOTVS Educacional quando são adicionadas bolsas no contrato do aluno, cujo a soma do seu percentual ultrapassem 100% de descontos o sistema emite um alerta bloqueando a adição desta bolsa.

*Exemplo:*Parcela: R$ 1000,00

Bolsa 1            50%                       
Bolsa 2            60%                
Total               110% de bolsa

Ao tentar inserir a segunda bolsa de 60% o sistema irá emitir um alerta, pois o total de bolsas neste caso ultrapassa o valor permitido de 100%, sendo assim esta bolsa não é inserida no contrato.  
Para que essa regra surja efeito, o sistema deve estar parametrizado para que a  esteja por "**contrato**" e o tipo de classificação seja igual a "**somar bolsas**". Veja mais sobre estes parâmetros clicando . Porém existe uma exceção na regra para que as bolsas que contenham fórmula parametrizada não sejam levadas em consideração no somatório dos percentuais da bolsa, pois este percentual será customizado pela própria fórmula cadastrada na bolsa e nesse caso a regra estará na fórmula. Veja mais sobre bolsa por fórmula clicando [aqui](http://tdn.totvs.com/pages/viewpage.action?pageId=354469739).

1
complete
**Período de competência contábil no processo de inclusão da Bolsa**

No processo de Inclusão de Bolsa é possível informar o Período de competência contábil para bolsa, assim ao incluir a bolsa no contrato essa data já será preenchida.

Caso o período de competência contábil já estiver preenchido no cadastro da **Bolsa | Bolsas por período letivo** essa data virá automaticamente no processo, mas terá também a opção de alterar esse período antes de Adicionar a bolsa.
