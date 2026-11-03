---
content_hash: 32c46f9422b147ec8bc19028b51c2e56f992efd74108a4ff2f8d2b48d3b3697e
fetched_at: '2026-06-29T00:11:59.610028+00:00'
page_id: '874206848'
product: rm
source: tdn-rm
title: 15- Biblioteca
type: documentation
url: https://tdn.totvs.com/display/LRM/15-+Biblioteca
version: 13
---

# Sumário

---

Sumário

# Menu da biblioteca

---

Os menus da biblioteca correspondem aos recursos do **TOTVS Bibliotecária** aos quais o professor terá acesso. No entanto, esses recursos estão disponibilizados no ..

Ao acessar qualquer um desses menus, o usuário será redirecionado, já autenticado, diretamente para o recurso no , em uma nova aba.

É importante ressaltar que as   de acesso seguem as mesma regras relatadas no .

# Parametrização

---

Para o correto funcionamento dos menus da biblioteca no Portal do Professor, é necessário configurar a URL **FrameHTML** nos parâmetros globais ou adicionar a tag **urlFrameHTML** no arquivo **config.json** do Portal do Professor, indicando o caminho base da instalação do FrameHTML.

Caso seja utilizado a tag **urlFrameHTML** no arquivo **config.json** do Portal do Professor, a mesma deve ser informada nesse local C:\TOTVS\CorporeRM\FrameHTML\Web\App\Edu\PortalDoProfessor\config.

A tag **urlFrameHTML**  deve ser passada dessa forma no arquivo, "urlFrameHTML": "[http://**\*EndereçoDaInstituição\***/FRAMEHTML/](http://localhost/FRAMEHTML/)", segue print de como deve ficar no arquivo.
