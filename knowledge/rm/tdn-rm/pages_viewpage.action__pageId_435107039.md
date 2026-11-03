---
content_hash: 19ba8f4643c88735354e3b2c8fbc8323a120e6bd2a893c1ba3ba5d92b8a25b6f
fetched_at: '2026-06-29T00:09:50.691485+00:00'
page_id: '435107039'
product: rm
source: tdn-rm
title: S-2230 - Como cadastrar mais de um atestado para o mesmo afastamento?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435107039
version: 6
---

---

Com a necessidade de vincular a um único afastamento vários atestados médicos e conforme já previsto pelo layout do eSocial, foi disponibilizado um anexo no cadastro do afastamento, onde se torna possível realizar essa vinculação.

Obs.: Nesse cenário, o grupo "infoAtestado" e seu filho "emitente" poderá se repetir dentro do XML até 9 vezes.

1true1PermissãoPermissão

Para que o anexo "Informações dos Atestados Médicos" fique visível na edição do afastamento, deverá ser dado permissão ao perfil (Serviços Globais | Segurança | Perfis) que se encontra associado ao usuário.

2CadastroCadastro

Além da permissão de visualização do anexo, para que o mesmo fique disponível para utilização deverá ser habilitado a flag "Afastamento com Diversos Atestados", assim o sistema passará a considerar as informações presentes no anexo que será liberado.

Aqui será listado todos os atestados já vinculados ao afastamento, vale ressaltar que será possível incluir apenas 9.

3Geração do XMLGeração do XML

Ao gerar o XML do afastamento que possuir mais de um atestado médico, o mesmo será representado conforme print abaixo, onde o grupo "infoAtestado" passa a se repetir junto com os grupos filhos.

4Consolidação no TAFConsolidação no TAF

Ao realizar a integração com o TAF, as informações referente aos atestados serão consolidadas no agrupamento "Informações do Atestado".

falsefalse

**Produto:** Folha de Pagamento

false

**Rotina:** eSocial

false

**Versões:**

|  |
| --- |
| 12.1.22 |
| 12.1.21 |
| 12.1.20 |

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
