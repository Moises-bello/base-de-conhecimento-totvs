---
content_hash: a381ea49680022ea9fe158c8c8f7686aee317cabeeaeb85fa6300a51635834b8
fetched_at: '2026-06-29T00:09:20.016677+00:00'
page_id: '422545632'
product: rm
source: tdn-rm
title: Outros Débitos/Créditos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545632
version: 18
---

**Informamos que os dados pessoais contidos nesta entidade foram colhidos para emissão de documentos fiscais e geração de rotinas legais e são retidos por determinação legal de normas fiscais e de transparência. Os mesmos não poderão ser eliminados em virtude de obrigação legal de retenção. O cumprimento de obrigação legal é hipótese legítima do tratamento dos seus dados conforme a Lei Geral de Proteção de Dados Pessoais (Lei n° 13.709/2018).**

**Para mais informações sobre a LGPD e as soluções oferecidas pela TOTVS consulte nossa página neste link ([https://tdn.totvs.com/pages/releaseview.action?pageId=514427789](https://tdn.totvs.com/pages/releaseview.action?pageId=514427789 "Follow link")).**

Ao final de cada apuração (ICMS e IPI), são necessários alguns ajustes devido a "outros lançamentos", como multas, estorno de débitos ou estorno de créditos.  
A denominação "Outros Débitos/Créditos" para esta tabela é default do sistema e pode ser alterada através do parâmetros da apuração de [tributos](http://tdn.totvs.com/display/LRM/Tributos).  
É permitida também a inclusão de Outros Débitos e Créditos para os demais Tributos cadastrados no TOTVS Gestão Fiscal.  
  
**Campo Classificação:**  
  
O Campo Classificação será exibido para todos os estados através de um campo livre exceto para os Estados do Paraná, Ceará, Amapá e Mato Grosso do Sul, estes vão possuir uma lista com opções já definidas.  
  
Para a geração automática do Lançamento de Outros Débitos/Créditos, o campo Observação será gerado default com a seguinte informação:

* **Para Tipo Débito**: Débito Diferencial de Alíquota
* **Para Tipo Crédit**o: Crédito Diferencial de Alíquota

IMPORTANTE!

Se tratando de Filial com endereço do estado de São Paulo, na inclusão automática dos Lançamentos de Outros Débitos e Créditos referente ao Diferencial de alíquotas, o campo ***Observação*** será preenchido com a seguinte expressão:

* No lançamento de crédito - "Inciso I do Art. 117 do RICMS",
* No lançamento de débito - "Inciso II do Art. 117 do RICMS".

O campo Sub Apuração do Período será exibido somente para lançamentos cujo tributo seja ICMS ou ICMSST. O mesmo será utilizado para a geração dos Registros 1921, 1922, 1923 e 1925 do SPED Fiscal.

### Contribuição Previdenciária

Para atender Ajustes e Exclusões no R-2060  da Reinf, para que apuração do imposto considere o Lançamento de Ajuste no momento em que for realizar o cálculo da Contribuição Previdenciária, destacando os valores dos ajustes por código de atividade, foi incluído no Lançamento de Outros Débitos/Créditos o campo de ID da Atividade Econômica. Este campo estará disponível somente para o tributo de CPRB a partir da versão 12.1.27.
