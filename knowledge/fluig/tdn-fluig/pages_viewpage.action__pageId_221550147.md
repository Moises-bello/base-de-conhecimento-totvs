---
content_hash: 9f3a53a21516cce310709f1a9a500a665f947c4136c276bcf7ce8a6e4d60b6d4
fetched_at: '2026-06-28T21:35:19.693388+00:00'
page_id: '221550147'
product: fluig
source: tdn-fluig
title: ARQ - Mensagem "-3 Data de expiracao invalida" ao acessar o login da plataforma
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=221550147
version: 7
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

# Ocorrência

Ao acessar a página de login da plataforma é exibido o erro "**-3 Data de expiracao invalida**". Como resolver?

# Causas e soluções

| Causas | Soluções |
| --- | --- |
| As licenças da plataforma estão vencidas. | A solução pode ser a atualização manual do licenciamento TOTVS.  Clique no botão que fica no topo superior direito do LS (License Server Monitor).   Ao pressionar este botão, o sistema automaticamente irá se conectar à TOTVS e atualizar as licenças com base no contrato TOTVS. |
| A plataforma está apontando para um servidor de LS inválido ou desatualizado. | Altere nas configurações globais o *hostname* ou IP do License Server para apontar para o endereço correto (geralmente é o mesmo servidor onde é executado o License Server Monitor). |

Utilize esta opção sempre que realizar a distribuição, manutenção e ou aquisição de licenças junto a TOTVS. Esta opção irá acelerar o processo de atualização das licenças com base nas modificações que você realizou no Portal do Cliente. Caso não seja realizado, a atualização ocorrerá durante o horário preestabelecido pela TOTVS.

Atenção!

Se o seu ambiente está no Cloud da TOTVS, a equipe de Cloud deverá fazer essa configuração.

# Observações

Para maiores informações a respeito do LS acesse .
