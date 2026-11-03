---
content_hash: 4f12861e924c0c1ddfdaff220492bf8f3f8327a0cee864646aa3fe4107db388a
fetched_at: '2026-06-29T00:10:07.316273+00:00'
page_id: '452719399'
product: rm
source: tdn-rm
title: Configuração de Registro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719399
version: 2
---

Etapa utilizada para configurar a ficha de Registro do Funcionário.  
    
    
 **Parâmetros**  
 Número da Ficha de Registro gerado pelo Sistema  
 Este parâmetro é utilizado para empresas que contém Ficha de Registro Informatizada. Ao confirmar esta opção não será permitida a inclusão ou edição do campo 'Nro. Ficha de Registro' do cadastro de funcionário e o número da ficha de registro do funcionário será gerado automaticamente pelo sistema em ordem sequencial.

**Observação**

O sistema faz validação de número de ficha duplicada, não permitido atribuir um número já pertencente a outro funcionário.   
 Numeração especifica para cada CNPJ  
 Com este parâmetro marcado, o sistema fará o controle automático do número de ficha de registro por CNPJ. Ou seja, no momento da inclusão de um novo funcionário o sistema identificará o número imediatamente posterior ao último da ficha de registro disponível para o CNPJ da seção em que o funcionário está sendo incluído e registrará este número no campo 'Nro. Ficha de Registro' do cadastro do funcionário.

**Observação**

Este parâmetro só fica habilitado se o parâmetro 'Número da Ficha de Registro gerado pelo Sistema' estiver marcado.  
 Não cadastrar número de Ficha de Registro para Estagiários e Autônomos  
 Com este parâmetro marcado, o Campo Nro. Ficha de Registro fica desabilitado para edição quando o tipo de funcionário for igual a 'T' (estagiário) ou 'A' (autônomo) e não gera o número de ficha de registro automático.   
    
 Não cadastrar número de Ficha de Registro para Diretores  
 Com este parâmetro marcado, o Campo Nro. Ficha de Registro fica desabilitado para edição quando o tipo de funcionário for igual a 'D' (Diretor) e não gera o número de ficha de registro automático.   
    
 Não cadastrar número de Ficha de Registro para Estatutários  
 Com este parâmetro marcado, o Campo Nro. Ficha de Registro fica desabilitado para edição quando o tipo de funcionário for igual a 'E' (Estatutário) e não gera o número de ficha de registro automático.  
    
 Não cadastrar número de Ficha de Registro para Temporários  
 Com este parâmetro marcado, o Campo Nro. Ficha de Registro fica desabilitado para edição quando o tipo de funcionário for igual a 'P' (Temporário) e não gera o número de ficha de registro automático.

**Observação**  
 Este parâmetro não considera os tipos 'B' (Temporário com redução de encargos) e 'F' (Temporário/Comissionista)

|  |  |
| --- | --- |
|  | Informações Complementares |

---

<< Retornar para **Folha de Pagamento**
