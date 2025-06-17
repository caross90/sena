package co.edu.sena.projectAppApex;


import co.edu.sena.projectAppApex.Model.Cliente;
import co.edu.sena.projectAppApex.Repository.ClienteRepository;
import co.edu.sena.projectAppApex.Service.ClienteService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

public class ClienteTest {
    ClienteRepository clienteRepository;
    ClienteService clienteService;

    @BeforeEach
    void setUp(){
        this.clienteRepository = mock(ClienteRepository.class);
        this.clienteService = new ClienteService(clienteRepository);
    }

    @Test
    void testCrearUsuario() {
        Cliente cliente = new Cliente(/* ... */);
        when(clienteRepository.save(any(Cliente.class))).thenReturn(cliente);

        Cliente nuevoCliente = clienteService.crearUsuario(cliente);

        assertEquals(cliente, nuevoCliente);
        verify(clienteRepository, times(1)).save(cliente);
    }

    @Test
    void testObtenerUsuarioPorGuiaExistente() {
        int guia = 1;
        Cliente cliente = new Cliente(/* ... */);
        when(clienteRepository.findById(guia)).thenReturn(Optional.of(cliente));

        Cliente resultado = clienteService.obtenerUsuarioPorGuia(guia);

        assertEquals(cliente, resultado);
        verify(clienteRepository, times(1)).findById(guia);
    }

    @Test
    void testObtenerUsuarioPorGuiaNoExistente() {
        int guia = 1;
        when(clienteRepository.findById(guia)).thenReturn(Optional.empty());

        Cliente resultado = clienteService.obtenerUsuarioPorGuia(guia);

        assertNull(resultado);
        verify(clienteRepository, times(1)).findById(guia);
    }

    @Test
    void testObtenerTodosLosClientes() {
        List<Cliente> clientes = new ArrayList<>();
        // Agregar clientes a la lista
        when(clienteRepository.findAll()).thenReturn(clientes);

        List<Cliente> resultado = clienteService.obtenerTodosLosClientes();

        assertEquals(clientes, resultado);
        verify(clienteRepository, times(1)).findAll();
    }

    @Test
    void actualizarCliente() {
        Integer guia = 12345;
        // Arrange
        Cliente clienteExistente = new Cliente(guia, "Maria", "calle 5a", 320495);
        when(clienteRepository.findById(guia)).thenReturn(Optional.of(clienteExistente));

        // Act
        Cliente clienteActualizado = new Cliente();
        clienteActualizado.setGuia(123456);
        clienteActualizado.setNombre("Nuevo Nombre");
        clienteActualizado.setDireccion("Nueva Dirección");
        clienteActualizado.setTelefono(123456789);

        Cliente clienteActualizado2 = clienteService.actualizarCliente(clienteActualizado);

    }

    @Test
    void eliminarCliente() {

        Integer guia = 1;
        doNothing().when(clienteRepository).deleteById(guia);

        clienteService.eliminarClientePorGuia(guia);

        verify(clienteRepository, times(1)).deleteById(guia);

    }
}
