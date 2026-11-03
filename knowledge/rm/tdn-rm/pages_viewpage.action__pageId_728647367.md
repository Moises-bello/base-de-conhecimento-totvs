---
content_hash: 95ce83f766e01b122723d8760ab8d17cf38f98eff7d461462a1fce0125c6a392
fetched_at: '2026-06-29T00:11:27.670852+00:00'
page_id: '728647367'
product: rm
source: tdn-rm
title: Código de cálculo 0043 x Banco de Horas e Alteração de Atitude
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=728647367
version: 17
---

**Observação:** Para que os eventos com código de cálculo 0043 sejam considerados no banco de horas, será necessário definir sua atitude nos parâmetros do Sindicato. Para configurar a atitude é necessário definir na etapa banco de horas opção: Considerar atitude do evento.

Alterar Atitude de ocorrências vinculadas ao código de cálculo 0043

Quando uma ocorrência customizada ou padrão do produto está vinculada ao código de cálculo 0043, o produto não impede a alteração da atitude, se o banco de horas for diário por ocorrência.

 Entretanto, o lançamento do evento para banco de horas ou movimento com o total das horas que tiveram a atitude alterada, somente irá ocorrer quando o evento 0043 está configurado com o tipo de faixa:  Número de Horas por Período. Além desta configuração o tipo de faixa de extras deve ser definida como Período.

*Ao utilizar a configuração do tipo de faixa: Tudo ou Intervalo a alteração de atitude não terá efeito para o número de horas no movimento ou banco de horas.*

Modificação de ocorrências vinculadas ao código de cálculo 0043

Caso deseje alterar a atitude da ocorrência parcial ou total pelo processo de modificação de ocorrência, deverá ser feita a modificação de ocorrência por intervalo, quando se trabalha considerando atitude por evento no sindicato vinculado ao funcionário. Além desta configuração o tipo de faixa de extras deve ser definida como Período. 

*Ao cadastrar a modificação de Ocorrência por número de horas, a alteração não terá efeito para o número de horas lançados no movimento ou banco de horas.*

 

11Exemplo 1

Será demonstrada a alteração da atitude da ocorrência Coletada.

Nos parâmetros do sindicato aba Banco de horas etapa **3-Faixas de Extras** o Tipo de faixa **"Período"** esta marcado.

Na etapa **13-Banco de horas** o parâmetro **"Considera atitude do evento"** esta marcado.

Na **etapa 18-Eventos**, editar o evento que possui o código de cálculo 0043,  definir o tipo da Faixa na aba Informações Adicionais.

.

O colaborador possui 2 horas a compensar.

Será definido que 1h10m serão pagas e o restante irá para o banco.

Realizado o recálculo com o parâmetro "Atualiza informações das ocorrências, desmarcado, será demonstrada mais de um tipo de ocorrência.

No Espelho terá as seguintes informações:

**Saldo Banco de Horas sintético**

**Saldo Banco de Horas Analítico**

**Banco de Horas**

**Movimento**

**Movimento diário**

**Ocorrências**

2Exemplo 2

Será demonstrada a alteração da Atitude pela Modificação de ocorrências.

Nos parâmetros do sindicato aba Banco de horas etapa **3-Faixas de Extras** o Tipo de faixa **"Período"** esta marcado.

Na etapa **13-Banco de horas** o parâmetro **"Considera atitude do evento"** esta marcado.

Na **etapa 18-Eventos** , editar o evento que possui o código de cálculo 0043 definir o tipo de ocorrências na aba Informações Adicionais.

O colaborador possui 2 horas a compensar.

Será definido que 1h será paga e o restante permanecerá como compensar (Banco de horas).

**Modificação de Ocorrências**

Realizado o recálculo com todos os parâmetro de calculo marcados.

No Espelho terá as seguintes informações:

**Saldo Banco de Horas sintético**

**Saldo Banco de Horas Analítico**

**Banco de Horas**

**Movimento**

**Movimento diário**

**Ocorrências**

**05. ASSUNTOS RELACIONADOS**

**.**
